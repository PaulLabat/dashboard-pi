# -*-coding:Utf-8 -*
from os import system
import xml.etree.ElementTree as ET

def getMeteo():
	return """<div id="cont_MzgxODV8NXw0fDR8NHwwMDAwMDB8MXxGRkZGRkZ8Y3wx"><div id="spa_MzgxODV8NXw0fDR8NHwwMDAwMDB8MXxGRkZGRkZ8Y3wx"><a id="a_MzgxODV8NXw0fDR8NHwwMDAwMDB8MXxGRkZGRkZ8Y3wx" href="http://www.meteocity.com/france/grenoble_v38185/" target="_blank" style="color:#000;text-decoration:none;">Météo Grenoble</a></div><script type="text/javascript" src="http://widget.meteocity.com/js/MzgxODV8NXw0fDR8NHwwMDAwMDB8MXxGRkZGRkZ8Y3wx"></script></div> """


def getMeteoYahoo():
	return system('curl "http://weather.yahooapis.com/forecastrss?w=22144181&u=c" >> orly.xml')

def recupMeteo():
	"""Parcours le fichier xml récupéré, puis renvoie les attribus dans cet ordre : condition,wind,atmospher,astronomy,forecast"""

	indiceDict=0
	forecast = dict()
	res = getMeteoYahoo()
	
	if res ==0:
		tree = ET.parse("orly.xml")
		root = tree.getroot()
		for elem in root.getiterator():
			if (elem.tag =="{http://xml.weather.yahoo.com/ns/rss/1.0}condition"):
				condition = elem.attrib
			if(elem.tag =="{http://xml.weather.yahoo.com/ns/rss/1.0}wind"):
				wind = elem.attrib
			if(elem.tag == "{http://xml.weather.yahoo.com/ns/rss/1.0}atmosphere"):
				atmospher = elem.attrib
			if(elem.tag == "{http://xml.weather.yahoo.com/ns/rss/1.0}astronomy"):
				astronomy = elem.attrib

			if(elem.tag == "{http://xml.weather.yahoo.com/ns/rss/1.0}forecast"):
				indiceDict += 1
				forecast[indiceDict] = elem.attrib

	return condition,wind,atmospher,astronomy,forecast


#liste les directions avec la signification :
#90 : E

def ecritMeteo(pagehtml):
	i=1
	#code pour meteo
	#pagehtml.write('<div id="meteo">{}</div>\n'.format(getMeteo()))
	#nouveau code
	condition,wind,atmospher,astronomy,forecast = recupMeteo()
	#print(condition)
	#print(wind)
	#print(atmospher)
	#print(astronomy)
	#print(forecast)
	pagehtml.write('<div id="meteo">\n')
	pagehtml.write('<div id="headmeteo">Aéroport Paris Orly</div>\n')
	pagehtml.write("<h1>Aujourd'hui {}°</h1>\n".format(condition["temp"]))#température actuel
	pagehtml.write('<div id="forecast"><h2>Prévisions</h2>\n')#debut ecriture des prévisions
	while i <= 5 :
		pagehtml.write(' {} {}° {}° {}</br>\n'.format(forecast[i]["day"],forecast[i]["low"],forecast[i]["high"], forecast[i]["text"]))
		i+=1

	pagehtml.write('</div>\n')

	pagehtml.write('<div id="details"> <h2> Détails</h2>\n')
	pagehtml.write('Température ressentie {}° Humidité {}% Pression {}mBar<br>\n'.format(wind["chill"], atmospher["humidity"],atmospher["pressure"]))
	pagehtml.write('Vent {}km/h Direction {}<br>\n'.format(wind["speed"],wind["direction"]))
	pagehtml.write('Visibilité {}km<br>\n'.format(atmospher["visibility"]))
	pagehtml.write('Levé {} Couché {}<br>\n'.format(astronomy["sunrise"],astronomy["sunset"]))
	pagehtml.write('</div>\n')

	pagehtml.write("</div>")

	#pour forecast, les indices du dico sont hight,code,low,date,text,day
	#changer la couleur du texte des données et pas des textes de précisions (tp0, humidité ...)