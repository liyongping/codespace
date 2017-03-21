# -*- coding: utf-8 -*-

'''
Download corresponding materials' pdf file from 121talk.com
'''


from bs4 import BeautifulSoup
import urllib2

base_url = "http://class.yeko.org.cn/Public/Uploads/Materials/"

select_str = '<select class="mid" name="mt_id"><option value="1003336" pdf="56025452216b1.pdf">Business English Preface</option><option value="1003337" pdf="560254ced9b2a.pdf">unit1 The first day at work</option><option value="1003338" pdf="566a3882dd2be.pdf">unit2 2.1 Asking for sick leave</option><option value="1003339" pdf="560254ebdf35b.pdf">unit2 2.2 Asking for casual leave</option><option value="1003356" pdf="56025508df76b.pdf">unit2 2.3 Asking for Annual Leave</option><option value="1003357" pdf="56025518045d4.pdf">unit2 2.4 Be late for work</option><option value="1003340" pdf="560255b943b46.pdf">unit3 3.1 Job Transfer</option><option value="1003341" pdf="560255c57e0dc.pdf">unit3 3.2 Promotion</option><option value="1003342" pdf="560255d505a12.pdf">unit3 3.3 Dismissal</option><option value="1003343" pdf="560255e9507f2.pdf">unit4 4.1 Ask for help</option><option value="1003344" pdf="560255fadfdf6.pdf">unit4 4.2 Invitation</option><option value="1003345" pdf="5602563596948.pdf">unit5 5.1 Expressing Gratitude</option><option value="1003346" pdf="5602564348cfe.pdf">unit5 5.2 Apology</option><option value="1003347" pdf="560256534828a.pdf">unit6 6.1 Application</option><option value="1003348" pdf="560256c078061.pdf">unit6 6.2 Congratulating a coworker</option><option value="1003349" pdf="560257168bf12.pdf">unit7 Business Conference</option><option value="1003350" pdf="5602573a1ae15.pdf">unit8 8.1 Dress Code</option><option value="1003351" pdf="5602575cf1a3a.pdf">unit8 8.2 Entertaining Clients</option><option value="1003352" pdf="5602576c6f156.pdf">unit9 9.1 Boarding</option><option value="1003353" pdf="5602577b6663b.pdf">unit9 9.2 Checking-in the hotel</option></select>';

# setup proxy
proxy = urllib2.ProxyHandler({'http': 'example.com:80'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)


ptag = BeautifulSoup(select_str)
for option in ptag.find_all('option'):
    class_name =  option.get_text()
    pdf_url = base_url + option["pdf"]
    print "Download: " + class_name, "url: " + pdf_url,

    #download the corresponding pdf file as class pdf file
    pdf_file = urllib2.urlopen(pdf_url)
    with open(class_name + '.pdf','wb') as output:
        output.write(pdf_file.read())
    print " Done"

