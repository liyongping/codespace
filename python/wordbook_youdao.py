# -*- coding: utf-8 -*-

'''
Utility for word book of youdao
'''

import os, sys
import urllib2
import mp3play
import time
from xml.etree import ElementTree as ET

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

def play_words(words=[], folder=None, dwell_time=1):
    '''
    Play words list.
    '''
    for word in words:
        word_file_name = word+".mp3"
        if folder is not None:
            word_file_name = os.path.join(folder, word_file_name)
        play_mp3(word_file_name)
        time.sleep(dwell_time)

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

def main():
    #setup_proxy_for_urllib2({'http': 'www.example.com:80'})
    xml_file_name = os.path.join('wordbook', "words.xml")

    words = extract_words_from_xml(xml_file_name)

    download_words(words, "wordbook")

    play_words(words, "wordbook")

if __name__ == '__main__':
    main()
