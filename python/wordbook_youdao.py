# -*- coding: utf-8 -*-

'''
Utility for word book of youdao
'''

import os, sys
import urllib2
import time
import argparse
from xml.etree import ElementTree as ET
from random import shuffle

import mp3play

def setup_proxy_for_urllib2(proxies=None):
    '''
    Setup proxy for urllib2
    '''
    if proxies is not None:
        proxy = urllib2.ProxyHandler(proxies)
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)

def download_word(word_name, folder=None):
    '''
    Download one word, and save it as "folder/word.mp3"
    '''
    # type 1: English
    # type 2: American
    base_url = 'http://dict.youdao.com/dictvoice?audio='+word_name+'&type=2'
    download_mp3(base_url, word_name+".mp3", folder)

def download_words(words=[], folder=None):
    '''
    Download words into "folder"
    '''
    for word in words:
        download_word(word, folder)

def download_mp3(url, saved_name, folder=None):
    '''
    Download one mp3 file which would be save as saved_name
    '''
    file_patch_name = saved_name
    if folder is not None:
        if not os.path.exists(folder):
            os.makedirs(folder)
        file_patch_name = os.path.join(folder, saved_name)
    #urllib.urlretrieve('http://dict.youdao.com/dictvoice?audio=safari&type=1', "safari.mp3")
    mp3_file = urllib2.urlopen(url)
    with open(file_patch_name, 'wb') as output:
        output.write(mp3_file.read())


def play_mp3(filename, max_seconds=5):
    '''
    Play one mp3 file
    '''
    clip = mp3play.load(filename)

    clip.play()
    # Let it play for up to 5 seconds, then stop it.
    time.sleep(min(max_seconds, clip.seconds()))
    clip.stop()

def play_words(words=[], folder=None, interval=1, play_mode="order", replay_times=1):
    '''
    Play words list.
    '''
    if play_mode == "random":
        shuffle(words)

    for word in words:
        word_file_name = word+".mp3"
        if folder is not None:
            word_file_name = os.path.join(folder, word_file_name)
        for _ in range(0,replay_times):
            play_mp3(word_file_name)
            time.sleep(interval)

def extract_words_from_xml(xml_file_name):
    '''
    Extract words from xml file which is exported from youdao.
    The return words list is sorted.
    '''
    per=ET.parse(xml_file_name)
    items = per.findall('./item')
    words = []
    for item in items:
        word = item.find('word').text
        words.append(word)
    words.sort()
    return words

def parse_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='workbook_name', type=file, required=True,
                        help='The workbook xml file')

    parser.add_argument('-m', '--mode', dest='mode', choices=['flush', 'play'], default='play',
                        help='Flush: Download all words to be local\n\
                                                      play : Play words\
                        ')
    parser.add_argument('-d', '--directory', dest='directory', default='wordbook',
                        help='Flush words.mp3 into this directory')
    parser.add_argument('-p', '--play', dest='play_mode', choices=['order', 'random'], default='order',
                        help='Play mode\n\
                              order : In order to play words\n\
                              random: Play words randomly\
                        ')
    parser.add_argument('-r', '--replay', dest='replay_times', type=int, default=3,
                        help='Replay times of every words')
    parser.add_argument('-i', '--interval', dest='interval', type=int, default=3,
                        help='The interval seconds of playing words')
    parser.add_argument('--http_proxy', dest='http_proxy',
                        help='Setup HTTP proxy')

    args = parser.parse_args()

    return args

def main():
    args =  parse_options()
    print args
    if args.http_proxy is not None:
        setup_proxy_for_urllib2({'http': args.http_proxy})

    words = extract_words_from_xml(args.workbook_name)
    print words
    if args.mode == 'flush':
        download_words(words, args.directory)
    elif args.mode == 'play':
        play_words(words, args.directory, args.interval, args.play_mode, args.replay_times)

if __name__ == '__main__':
    main()
