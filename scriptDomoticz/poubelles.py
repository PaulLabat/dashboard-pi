#! /usr/bin/python2.7
# -*-coding:Utf-8 -*

import urllib2
from bs4 import BeautifulSoup


def getPoubelles():
	dico = dict()
	i=1
	try:
		url = urllib2.urlopen('http://www.portesessonne.fr/Vivre-et-entreprendre/Dechets/Quand-sortir-mes-poubelles', "BuildingType=1&LoadStreetsUrl=%2Fsdform%2Fload_street&City=2&Street=219&SubitRequestSmallButton=")
	except IOError:
		print("Impossible de récupérer les données pour les poubelles.")
		return None
	else:
		soup = BeautifulSoup(url.read())
		for td in soup.find_all('td'):
			dico[i] = td.string.encode("utf-8")
			i = i+1
		return dico

		
if __name__ == '__main__':
	dico = getPoubelles()
	if dico is not None:
		for elm in dico.values():
			print(elm)
