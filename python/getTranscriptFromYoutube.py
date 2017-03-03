#-*-coding:utf-8-*-

import urllib;
import urllib2;
import BeautifulSoup

class Robot:
    def __init__(self, url):
        self.url = url
    def GetPageContent(self, url):
        self.pageContent = ""
        #u = urllib.urlopen(url, proxies={'http':'http://cn-proxy.jp.oracle.com:80'})
        
        proxy_handler = urllib2.ProxyHandler({"http" : 'http://cn-proxy.jp.oracle.com:80'})
        opener = urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)
        u = urllib2.urlopen(url)
        if u.getcode() == 200:
            try:
                pageContent = u.read()
            finally:
                u.close()
    def GetTranscriptDIV(self):
        oup = BeautifulSoup(self.pageContent)
        ul = soup.find('div',{'id':'transcript-scrollbox'})
        if not ul:
            return ""
        print ul
    def GetContent(self):
        self.GetPageContent(self.url)
        self.GetTranscriptDIV()
        
if __name__ == '__main__':
    r = Robot("https://www.youtube.com/watch?v=maYFI5O6P-8&index=6&list=PL2F07DBCDCC01493A")
    r.GetContent()