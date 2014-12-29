# -*-coding:Utf-8 -*

import subprocess
from bs4 import BeautifulSoup

def recupPrevision():
	res, error = subprocess.Popen(['curl','http://www.transilien.com/flux/rss/traficLigne?codeLigne=C'], stdout = subprocess.PIPE).communicate()

	if error is None:
		soup = BeautifulSoup(res)
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
	else:
		print('Erreur de récupération des prévisions de la ligne C')
		return None,None,None
	

def ecritTraficRer(html):
	title, description, pubdate = recupPrevision()
	if title is not None and description is not None and pubdate is not None:
		html.write('<h3 class="sub-header">{}</h3>\n'.format(title))
		html.write('{}<br><span style="font-size:10px;">{}</span>\n'.format(description,pubdate))

