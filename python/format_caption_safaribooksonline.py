from bs4 import BeautifulSoup


soup = BeautifulSoup(open("safari.xml"),"lxml")


for p in soup.find_all('p'):
    ptext= str(p).replace("<br/>", " ")
    print BeautifulSoup(ptext,"lxml").get_text()
