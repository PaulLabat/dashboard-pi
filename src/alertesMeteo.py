# -*-coding:Utf-8 -*

from os import system
from bs4 import BeautifulSoup
import urllib2

def getVigilance(departement):
	vigilance = ''
	date = ''
	try:
		if departement == 'essonne':
			url = urllib2.urlopen('http://www.meteoalarm.eu/fr_FR/0/0/FR066-Essonne.html')
		elif departement == 'haute_vienne':
			url = urllib2.urlopen('http://www.meteoalarm.eu/fr_FR/0/0/FR019-Haute_Vienne.html')
	except IOError:
		vigilance = "Impossible de récupérer les données pour la vigilance meteo."
	else:
		soup = BeautifulSoup(url.read())
		divinfo = soup.find_all('div',class_='info')
		for elem in divinfo:
			if elem.br == None:
				if not elem.text.find('Valable'):
					date = elem.text.encode('utf-8')
				else:
					vigilance = elem.text.encode('utf-8')

	return vigilance, date

def getColor(vigilance):
	if vigilance.find('Jaune') != -1:
		return 'Jaune'
	elif vigilance.find('Rouge')!= -1:
		return 'Rouge'
	elif vigilance.find('Orange')!= -1:
		return 'Orange'
	else:
		return 'Vert'


def ecritVigilance(departement, html):
	vigilance, date = getVigilance(departement)
	html.write('<h3 class="sub-header">Vigilance météo</h3>\n')
	html.write('<span class="{}">{}</span>'.format(getColor(vigilance),vigilance))
	if date != '':
		html.write('<br><span style="font-size:10px;">{}</span>'.format(date))

