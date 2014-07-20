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
		tmp = soup.find_all('title')
		if len(tmp) == 2:
			title = tmp[1].string.encode('utf-8')
		else:
			title = tmp[0].string.encode('utf-8')
		tmp = soup.find_all('description')
		if len(tmp) == 2:
			description = tmp[1].string.encode('utf-8')
		else:
			description = "Pas de perturbations"
		
		tmp = soup.find('pubdate')
		if tmp:
			pubdate = tmp.string.encode('utf-8')
		else:
			pubdate = ""
	return title, description, pubdate

def ecritTraficRer(html):
	title, description, pubdate = recupPrevision()
	html.write('<h3 class="sub-header">{}</h3>\n'.format(title))
	html.write('{}<br><span style="font-size:10px;">{}</span>\n'.format(description,pubdate))

