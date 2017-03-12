#!/usr/bin/env python 
#-*- coding: utf-8 -*- 
 
import urllib2 
import random
import time 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
 
class Vote: 
    def __init__(self, useId, pageId=1, proxy=""):         
        self.proxy = proxy 
        self.url = 'http://littlepoll.people.com.cn/2012ys/20120224button/tp.php?id='+useId+'&t=95953&type=362%20&callback=jQuery1710036934433168821945_1455885411649&_=1455885430049'
        self.timeout = 2
        self.pageId = pageId
 
    def run(self): 
        votetip = ""
        if len(self.proxy) > 8:
            proxy_handle = urllib2.ProxyHandler({"http": r'http://%s' % self.proxy}) 
            opener = urllib2.build_opener(proxy_handle) 
            urllib2.install_opener(opener) 
            votetip =  "Used proxy, "
        try: 
            request = self.getRequest()
            req = urllib2.urlopen(request, timeout=self.timeout)
            if req.getcode() == 200:
                print votetip + "1 vote has been voted successfully"
                addnum()
        except Exception,e: 
            #print e 
            pass  
    def getRequest(self):
        request = urllib2.Request(self.url)
        request.add_header('Accept-Encoding', 'gzip, deflate')
        request.add_header('Host', 'littlepoll.people.com.cn')
        referer = 'http://pic.people.com.cn/GB/54965/402337/index'+str(pageId)+'.html'
        request.add_header('Referer', referer)
        rvalue = str(random.randint(17, 42))
        useragent = r'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:'+ rvalue +'.0) Gecko/20100101 Firefox/'+ rvalue+ '.0'
        type = random.randint(1, 3)
        if type == 1:
            request.add_header('User-Agent', useragent)
            request.add_header('Accept', '*/*')
            request.add_header('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
        elif type == 2:
            request.add_header('User-Agent', useragent)
            request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
            request.add_header('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
        else:
            request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko')
            request.add_header('Accept', 'application/javascript, */*;q=0.8')
            request.add_header('Accept-Language', 'zh-CN')
        return request
 
def addnum(): 
    global n 
    n += 1
 
def shownum(): 
    return n 
 
n = 0

if __name__ == '__main__': 
    requestNumber = 0
    timeSleep = 0
    pageId = 1
    try:
        print u'请输入需要刷票的voteId：(一般为5位，如 38131)'
        useId = raw_input(); 
        print u'请选择当前的投票网址：（默认为 1）'
        print u'1 --- http://pic.people.com.cn/GB/54965/402337/index1.html'
        print u'2 --- http://pic.people.com.cn/GB/54965/402337/index2.html'
        print u'3 --- http://pic.people.com.cn/GB/54965/402337/index3.html'
        pageId = int(raw_input()); 
        if pageId < 1 or pageId > 3:
            print u'投票网址选择错误，采用默认的网址 1'
        
        print u'请输入需要刷取得票数：（默认一次100票）'
        requestNumber = int(raw_input());
        print u'请输入刷票间隔时间（单位秒，默认间隔1秒），0表示没有间隔，1表示1秒，以此类推：'
        timeSleep = int(raw_input());
        if timeSleep < 1:
            timeSleep = 0
    except Exception,e:
        print u'用户参数输入错误，尝试采用默认值'
        requestNumber = 100
        timeSleep = 1
        pageId = 1
        pass
    print u'即将为用户: ' + useId + ', 开始刷取: ' +str(requestNumber)+ ' 票' + ', 间隔时间为：' + str(timeSleep) +' 秒'

    if requestNumber < 1:
        print u'非法的刷票数，退出程序。'
        sys.exit()

    proxylist = []
    try:
        proxylist = open('proxy.txt', 'r').readlines();
    except Exception,e:
        pass

    if len(proxylist) > 0:
        print u'发现代理列表文件proxy.txt, 有 %s 个代理IP地址可用。' % len(proxylist)

    start_time = time.time() 
    while(shownum() < requestNumber):
        if len(proxylist) == 0:
            v = Vote(useId) 
            v.run();
            if timeSleep > 0:
                time.sleep(timeSleep)
        else:
            for proxy in proxylist: 
                v = Vote(useId,proxy) 
                v.run();
                if timeSleep > 0:
                    time.sleep(timeSleep)
                if shownum() == requestNumber:
                    break;

    print u'本次总共刷了 %s 票，耗时 %s 秒'  % (shownum(), time.time()-start_time)

    print u'请敲击任何按键，退出当前程序...'
    raw_input()