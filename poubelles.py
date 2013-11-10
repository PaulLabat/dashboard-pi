# -*-coding:Utf-8 -*
import urllib2
from bs4 import BeautifulSoup


def getPoubelles():
	fichier = open("poubelles.html",'w')
	dico = dict()
	i=1
	try:
		url = urllib2.urlopen('http://www.portesessonne.fr/Vivre-et-entreprendre/Dechets/Quand-sortir-mes-poubelles', "BuildingType=1&LoadStreetsUrl=%2Fsdform%2Fload_street&City=2&Street=219&SubitRequestSmallButton=")
	except IOError:
		print("Impossible de récupérer les données pour les poubelles.")
	else:
		soup = BeautifulSoup(url.read())
		for td in soup.find_all('td'):
			dico[i] = td.string
			i = i+1


	return dico

def ecritPoubelles(pagehtml):
	dico = getPoubelles()
	pagehtml.write('<div id="poubelles">\n')
	for elm in dico.values():
		#tmp = u"{}".format(elm)
		pagehtml.write(elm.encode("utf-8"))
		pagehtml.write("<br>\n")

	pagehtml.write('</div>\n')