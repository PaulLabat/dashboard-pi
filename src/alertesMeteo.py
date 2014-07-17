# -*-coding:Utf-8 -*

from os import system
from bs4 import BeautifulSoup
import urllib2

def getVigilance(departement):
	vigilance = ''
	try:
		if departement == 'essonne':
			url = urllib2.urlopen('http://www.meteoalarm.eu/fr_FR/0/0/FR066-Essonne.html')
		elif departement == 'haute_vienne':
			url = urllib2.urlopen('http://www.meteoalarm.eu/fr_FR/0/0/FR019-Haute_Vienne.html')
	except IOError:
		print("Impossible de récupérer les données pour les poubelles.")
	else:
		soup = BeautifulSoup(url.read())
		for elem in soup.find_all('div'):
			if elem.string is not None:
				vigilance = elem.string.encode('utf-8')

	return vigilance

def ecritVigilance(departement, html):
	vigilance = getVigilance(departement)
	html.write('<h3 class="sub-header">Vigilance meteo</h3>')
	html.write(str(vigilance))

