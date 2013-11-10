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

def getImage(code):
	return{
		"Shower Early":"img/icons_120x100/05d.png",
		"Partly Cloudy":"img/icons_120x100/03d.png"

	}[code]

def getDay(day):
	return{
	"Mon":"Lundi",
	"Tue":"Mardi",
	"Wed":"Mercredi",
	"Thu":"Jeudi",
	"Fri":"Vendredi",
	"Sat":"Samedi",
	"Sun":'Dimanche'
	}[day]


#liste les directions avec la signification :
#90 : E
#190 : S

def ecritMeteo(pagehtml):
	i=1
	#code pour meteo
	#pagehtml.write('<div id="meteo">{}</div>\n'.format(getMeteo()))
	#nouveau code
	condition,wind,atmospher,astronomy,forecast = recupMeteo()
	pagehtml.write('<div id="meteo">\n')
	pagehtml.write('<div id="headmeteo">Aéroport Paris Orly</div>\n')
	pagehtml.write('<div id="meteoJour">{}° <img src="img/icons_120x100/02d.png"></div>\n'.format(condition["temp"]))#température actuel
	pagehtml.write('<div id="forecast"><h2>Prévisions</h2>\n')#debut ecriture des prévisions
	pagehtml.write('<table>')
	pagehtml.write('<tr>\n<td>Jour</td> <td>Min</td> <td>Max</td> <td>Code</td>\n</tr>\n')
	while i <= 5 :
		pagehtml.write('<tr>\n<td>{}</td>\n'.format(getDay(forecast[i]["day"])))
		pagehtml.write('<td>{}°</td>\n'.format(forecast[i]["low"]))
		pagehtml.write('<td>{}°</td>\n'.format(forecast[i]["high"]))
		pagehtml.write('<td>{}</td>\n</tr>\n'.format(forecast[i]["code"]))


		i+=1

	pagehtml.write('</table>')
	pagehtml.write('</div>\n')

	pagehtml.write('<div id="details"> <h2> Détails</h2>\n')
	pagehtml.write("<table>\n")
	pagehtml.write('<tr>\n<td>Température ressentie</td> <td><b>{}°</b></td> <td>Humidité</td> <td><b>{}%</b></td>\n</tr>\n'.format(wind["chill"], atmospher["humidity"]))
	pagehtml.write('<tr>\n<td>Vent</td> <td><b>{}km/h</b></td> <td>Direction</td> <td><b>{}</b></td>\n</tr>\n'.format(wind["speed"],wind["direction"]))
	pagehtml.write('<tr>\n<td>Visibilité</td> <td><b>{}km</b></td> <td>Pression</td> <td><b>{}mBar</b></td>\n</tr>\n'.format(atmospher["visibility"],atmospher["pressure"]))
	pagehtml.write('<tr>\n<td>Levé</td> <td><b>{}</b></td> <td>Couché</td> <td><b>{}</b></td>\n</tr>\n'.format(astronomy["sunrise"],astronomy["sunset"]))
	pagehtml.write("</table>\n")
	pagehtml.write('</div>\n')

	pagehtml.write("</div>")

	#pour forecast, les indices du dico sont hight,code,low,date,text,day
	#changer la couleur du texte des données et pas des textes de précisions (tp0, humidité ...)