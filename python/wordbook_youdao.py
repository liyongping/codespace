# -*- coding: utf-8 -*-

'''
Utility for word book of youdao
'''

import os
import urllib2
import mp3play
import time

def setup_proxy_for_urllib2(proxies=None):
    if proxies is not None:
        proxy = urllib2.ProxyHandler(proxies)
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)

def download_word(word_name):
    # type 1: English
    # type 2: American
    base_url = 'http://dict.youdao.com/dictvoice?audio='+word_name+'&type=2'
    download_mp3(base_url, word_name+".mp3")

def download_words(words=[]):
    for word in words:
        download_word(word)

def download_mp3(url, saved_name, proxy=None):

    #urllib.urlretrieve('http://dict.youdao.com/dictvoice?audio=safari&type=1', "safari.mp3")
    mp3_file = urllib2.urlopen(url)
    with open(saved_name, 'wb') as output:
        output.write(mp3_file.read())


def play_mp3(filename, max_seconds=5):
    clip = mp3play.load(filename)

    clip.play()
    # Let it play for up to 5 seconds, then stop it.
    time.sleep(min(max_seconds, clip.seconds()))
    clip.stop()

def play_words(words=[], dwell_time=1):
    for word in words:
        play_mp3(word+".mp3")
        time.sleep(1)

#setup_proxy_for_urllib2({'http': 'www.example.com:80'})
words = ['your','me','safari','test']

download_words(words)

play_words(words)