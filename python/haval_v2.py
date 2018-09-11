# -*- coding: utf-8 -*-
import httplib;
import json;
import time;
import hashlib;
import random
import sys, getopt

def usage():
	print "haval.py --oid=<oid> --cookie=<cookie>"

def get_oid_cookie():
	oid = ""
	cookie = ""

	try:
		opts, args = getopt.getopt(sys.argv[1:], "ho:c:", ["oid=","cookie="])
	except getopt.GetoptError, err:  
	    print str(err)  
	    usage()  
	    sys.exit(2) 

	for op, value in opts:

		if op == "-o" or op == "--oid":
			oid = value
		elif op == "-c" or op == "--cookie":
			cookie = value
		elif op == "-h":
			usage()
			sys.exit()

	return (oid, cookie)

def md5_str(red_type, selected_car, timestamp, md5_key='zxcvbnm'):
	m = hashlib.md5();
	m.update(red_type + selected_car + timestamp + md5_key)
	return m.hexdigest()

def get_ts():
	ts = int(time.time())
	return str(ts*1000+608)

def request_one(red_type="purchase", selected_car="H7Blue"):

	#oid = "yFsm26vWYSyORr3as6t3vvmEblO0FtvGMjRwg2y9254"
	#cookie = "Hm_lvt_446349eb3c4d6919acfa93b92e7c453a=1489854055,1489890716; Hm_lpvt_446349eb3c4d6919acfa93b92e7c453a=1489890716; __wmv=1489854055.2; __wms=1489892517; PHPSESSID=0ldhe52o0ick4pvkda749tsrj5"
	oid, cookie = get_oid_cookie()
	#content0 = "car=H7Blue&ty=purchase&_t=1489824361133&_s=5c628b13d65a8a36245d7fd61faa9ee3";
	time_stamp = get_ts();
	md5_value = md5_str(red_type, selected_car, time_stamp);
	content = "car="+ selected_car + "&ty="+ red_type +"&_t="+ time_stamp +"&_s="+ md5_value;


	

	headers = {
		"Host": "cash.haval.com.cn",
		#"Content-Length": "75",
		"Accept": "application/json, text/javascript, */*; q=0.01",
		"Origin": "http://cash.haval.com.cn",
		"X-Requested-With": "XMLHttpRequest",
		"User-Agent": "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; OPPO R9s Build/MMB29M)",
		"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
		"Referer": "http://cash.haval.com.cn/?media=zmt",
		#"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "zh-CN,en-US;q=0.8",
		"Cookie": cookie,
		"Connection": "close"
		};

	conn = httplib.HTTPConnection("cash.haval.com.cn", 80);
	conn.request('POST', 
	             '/app/Lottery/index/oid/'+oid, 
	             content, 
	             headers);
	res = conn.getresponse();
	newheaders = res.getheaders();
	tmpmsg = res.read();
	if res.status == 200 and len(tmpmsg) > 160:
		son_obj = json.loads(tmpmsg)
		print "p: " + son_obj['data']['point']
		if int(son_obj['data']['point']) >= 2000:
			print "--------------------------!!!!"
		if int(son_obj['data']['point']) == 4999:
			print "success"
			conn.close();

			content = "carid=&name=%E6%9D%8E%E6%B0%B8%E5%B9%B3&ext%5Bprovince%5D=11%7C%E6%B1%9F%E8%8B%8F%E7%9C%81&ext%5Bcity%5D=111%7C%E8%8B%8F%E5%B7%9E%E5%B8%82&ext%5Bdealer%5D=320512%7C%E8%8B%8F%E5%B7%9E%E5%B8%B8%E5%9F%8E%E6%B1%BD%E8%BD%A6%E9%94%80%E5%94%AE%E6%9C%8D%E5%8A%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&rid=&carcode=H7Blue&ext%5Bclient%5D=m&ext%5Bmedia%5D=zmt&prize_id=94";
			conn = httplib.HTTPConnection("cash.haval.com.cn", 80);
			conn.request('POST', 
			             '/app/Lottery/save/oid/'+oid, 
			             content, 
			             headers);
			res = conn.getresponse();
			newheaders = res.getheaders();
			tmpmsg = res.read();
			if res.status == 200:
				print tmpmsg
			return 1

	conn.close();
	return 0



if __name__ == '__main__':
	
	for i in range(10000):
		if request_one() == 1:
			break;
		time.sleep(random.randint(4,5))