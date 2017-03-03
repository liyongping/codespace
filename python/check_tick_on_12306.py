# -*- coding: utf-8 -*-
'''
Created on 2012-5-16

@author: lyp
'''
import httplib2
import socks

#httplib2.debuglevel=4
h = httplib2.Http(".cache", disable_ssl_certificate_validation=True,
				proxy_info = httplib2.ProxyInfo(socks.PROXY_TYPE_HTTP, '----------', 80)
				)

headers = {'Host': 'kyfw.12306.cn',
'Connection': 'keep-alive',
'Cache-Control': 'no-cache',
'Accept': '*/*',
'X-Requested-With': 'XMLHttpRequest',
'If-Modified-Since': '0',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init',
'Accept-Encoding': 'gzip, deflate, sdch',
'Accept-Language': 'en-US,en;q=0.8',
#'Cookie': '__NRF=D448883EA47A42ADFF201315C5A47B59; JSESSIONID=0A02F035C43075CCEF5A53A5CF70F75AF760967AEC; BIGipServerotn=904921610.50210.0000; current_captcha_type=Z; _jc_save_fromStation=%u82CF%u5DDE%2CSZH; _jc_save_toStation=%u9F99%u5CA9%2CLYS; _jc_save_fromDate=2016-02-05; _jc_save_toDate=2015-12-10; _jc_save_wfdc_flag=dc'
}
response, content = h.request("http://kyfw.12306.cn/otn/leftTicket/queryT?leftTicketDTO.train_date=2016-02-05&leftTicketDTO.from_station=SZH&leftTicketDTO.to_station=LYS&purpose_codes=ADULT",
	 "GET", headers=headers)

if response['status'] == 200:
	print content
else:
	print "missing"