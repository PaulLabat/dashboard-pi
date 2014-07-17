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
	return title, description,

def ecritTraficRer(html):
	title, description = recupPrevision()
	html.write('<h3 class="sub-header">{}</h3>\n'.format(title))
	html.write(description)

