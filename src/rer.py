# -*-coding:Utf-8 -*


from os import system
from bs4 import BeautifulSoup

def getPresivion():
	return system('curl http://www.transilien.com/flux/rss/traficLigne?codeLigne=C > rer.xml')

def recupPrevision():
	res = getPresivion()
	if res == 0:
		f = open('rer.xml','r')
		soup = BeautifulSoup(f.read())
		f.close()
		title = soup.find_all('title')[1].string.encode('utf-8')
		description = soup.find_all('description')[1].string.encode('utf-8')
		pubdate = soup.find('pubdate').string.encode('utf-8')
	return title, description, pubdate

def ecritTraficRer(html):
	title, description, pubdate = recupPrevision()
	html.write('<h3 class="sub-header">{}</h3>\n'.format(title))
	html.write('{}<br><span style="font-size:10px;">{}</span>\n'.format(description,pubdate))

