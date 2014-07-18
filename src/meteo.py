# -*-coding:Utf-8 -*
from os import system
import xml.etree.ElementTree as ET

def getMeteoYahoo(woeid):
	return system('curl "http://weather.yahooapis.com/forecastrss?w='+woeid+'&u=c" > weather.xml')

def recupMeteo(woeid):
	"""Parcours le fichier xml récupéré, puis renvoie les attribus dans cet ordre : condition,wind,atmospher,astronomy,forecast"""

	indiceDict=0
	forecast = dict()
	res = getMeteoYahoo(woeid)
	
	if res ==0:
		tree = ET.parse("weather.xml")
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

def convertTime(time):
	split = time.split(' ')
	if split[1] == 'am':
		time = split[0]
	elif split[1] == 'pm':
		tmp = split[0].split(':')
		time = str(int(tmp[0])+12)+':'+tmp[1]
	return time

def ecritMeteo(pagehtml, woeid, city):
	i=1
	condition,wind,atmospher,astronomy,forecast = recupMeteo(woeid)
	pagehtml.write('<h1 class="header">'+city+'</h1>')
	pagehtml.write('<h3 class="sub-header">Prévisions</h3>\n')
	pagehtml.write('<table>\n<tr>\n')#debut du tableau qui englobe tout

	#prev aujourd'hui
	pagehtml.write('<td>\n<table style="width:120px;">\n')#table qui contient info 1 jour
	pagehtml.write("<tr>\n")
	pagehtml.write("<td>\n")
	pagehtml.write("<table>\n")
	pagehtml.write("<tr>\n<td>Maintenant </td></tr>\n")
	pagehtml.write("<tr>\n<td>\n")
	pagehtml.write('<table>\n<tr>\n')
	pagehtml.write("<td>{}°\n".format(condition["temp"]))
	pagehtml.write("</td>\n")
	pagehtml.write('<td><img src="../img/meteo/{}.png"/></td>\n'.format(condition["code"]))
	pagehtml.write('</tr>\n</table>\n')
	pagehtml.write("</td>\n</tr>\n</table>\n")
	pagehtml.write("</td>\n")
	pagehtml.write("</tr>\n")
	pagehtml.write("</table>\n")

	while i<=5:
		pagehtml.write('<td>\n<table style="width:120px;">\n')#table qui contient info 1 jour
		pagehtml.write("<tr>\n")
		pagehtml.write("<td>\n")
		pagehtml.write("<table>\n")
		pagehtml.write('<tr>\n<td> {} </td></tr>\n'.format(getDay(forecast[i]["day"])))
		pagehtml.write("<tr>\n<td>\n")
		pagehtml.write('<table>\n<tr>\n')
		pagehtml.write("<td>\n")
		pagehtml.write("<table>\n<tr>\n")
		pagehtml.write('<td> {}° </td>'.format(forecast[i]["high"]))
		pagehtml.write('</tr>\n<tr>\n')
		pagehtml.write('<td><span class="color"> {}° </span></td>'.format(forecast[i]["low"]))
		pagehtml.write("</tr>\n</table>\n")
		pagehtml.write("</td>\n")
		pagehtml.write('<td><img src="../img/meteo/{}.png"/></td>\n'.format(forecast[i]["code"]))
		pagehtml.write('</tr>\n</table>\n')
		pagehtml.write("</td>\n</tr>\n</table>\n")
		pagehtml.write("</td>\n")
		pagehtml.write("<td></td>\n")
		pagehtml.write("</tr>\n")
		pagehtml.write("</table>\n")
		i+=1

	pagehtml.write("</td>\n</tr>\n")
	pagehtml.write('</table>\n')#table englobante fin

	#******************************Details
	pagehtml.write('<table class="table table-striped" style="width:720px;">\n')
	pagehtml.write('<tr>\n<td>Température ressentie</td> <td><span class="color">{}°</span></td> <td>Humidité</td> <td><span class="color">{} %</span></td>\n</tr>\n'.format(wind["chill"], atmospher["humidity"]))
	pagehtml.write('<tr>\n<td>Vent</td> <td><span class="color">{} km/h</span></td> <td>Direction</td> <td><span class="color">{}</span></td>\n</tr>\n'.format(wind["speed"],wind["direction"]))
	pagehtml.write('<tr>\n<td>Visibilité</td> <td><span class="color">{} km</span></td> <td>Pression</td> <td><span class="color">{} mBar</span></td>\n</tr>\n'.format(atmospher["visibility"],atmospher["pressure"]))
	pagehtml.write('<tr>\n<td>Levé</td> <td><span class="color">{}</span></td> <td>Couché</td> <td><span class="color">{}</span></td>\n</tr>\n'.format(convertTime(astronomy["sunrise"]),convertTime(astronomy["sunset"])))
	pagehtml.write("</table>\n")
	
