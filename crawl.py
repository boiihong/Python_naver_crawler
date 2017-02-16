import urllib
import requests
from bs4 import BeautifulSoup
import codecs
import sys


def spider(i):
	_file = open('./school.txt', 'r')
	_file2 = open('./pn.txt','w')
	for line in _file.readlines() :
		line = unicode(line,'cp949', errors='ignore').encode('utf-8')
		line = " ".join(line.split())
		#print line
		url = 'http://search.naver.com/search.naver?where=nexearch&query='+ line + '&sm=top_hty&fbm=0&ie=utf8'
		print url
		#_file2.write(url)
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text, 'lxml')
		#print soup.prettify()
		#phone = soup.find_all('span')
		phone = soup.find("span",{"class": "tell"}).contents[0]
		#phone = soup.find("div",{"class":"local map" })
		print phone+ '\n'
		_file2.write(phone+'\n')
	_file.close()
	_file2.close()

reload(sys)
sys.setdefaultencoding('utf-8')
spider(1)
