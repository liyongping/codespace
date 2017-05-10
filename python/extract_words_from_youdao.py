#-*-coding:utf-8-*-
'''
Created on 2013-8-21

@author: vincent
'''
from xml.etree import ElementTree as ET

def getEnSt(str):
    result = u'';
    for x in str:
        if is_zh(x):
            continue
        else:
            result += x
    return result

def is_zh (c):
        x = ord (c)
        # Punct & Radicals
        if x >= 0x2e80 and x <= 0x33ff:
                return True

        # Fullwidth Latin Characters
        elif x >= 0xff00 and x <= 0xffef:
                return True

        # CJK Unified Ideographs &
        # CJK Unified Ideographs Extension A
        elif x >= 0x4e00 and x <= 0x9fbb:
                return True
        # CJK Compatibility Ideographs
        elif x >= 0xf900 and x <= 0xfad9:
                return True

        # CJK Unified Ideographs Extension B
        elif x >= 0x20000 and x <= 0x2a6d6:
                return True

        # CJK Compatibility Supplement
        elif x >= 0x2f800 and x <= 0x2fa1d:
                return True

        else:
                return False

if __name__ == '__main__':
    
    per=ET.parse('0821_wordbook.xml')
    items = per.findall('./item')
    words = []
    sentences = []
    for item in items:
        word = item.find('word').text
        words.append(word)
        sts = item.find('trans').text.split('-')
        if len(sts) > 1:
            st = getEnSt(sts[1])
            sentences.append(st)
    part_number = len(words)/100
    print "words:",len(words)
    for p in range(0,part_number):
        p100 = p*100
        p1100 = (p+1)*100
        filename = "words_%d-%d.txt"%(p100,p1100)
        file = open(filename,'w+')
        file.write("\n".join(words[p100:p1100]))
        file.close()

    part_number = len(sentences)/50
    print "sentences:",len(sentences)
    for p in range(0,part_number):
        p100 = p*50
        p1100 = (p+1)*50
        filename = "sentences_%d-%d.txt"%(p100,p1100)
        file = open(filename,'w+')
        file.write("\n".join(sentences[p100:p1100]))
        file.close()
    