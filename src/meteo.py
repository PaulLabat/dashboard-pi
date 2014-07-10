# -*-coding:Utf-8 -*
from os import system
import xml.etree.ElementTree as ET
from crueseine import recupAlerte, getDescription
from date import returnDate

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
	condition,wind,atmospher,astronomy,forecast = recupMeteo()
	alerte, dateMaj = recupAlerte()
	wday,mday,month,year,hour, minut = returnDate()


	pagehtml.write('<div id="meteo">\n')
	pagehtml.write('<div id="headmeteo">{} {} {} {} {}:{}</div>\n'.format(wday,mday,month,year,hour, minut))
	#debut ecriture des prévisions
	pagehtml.write('<div id="forecast"><h2>Prévisions</h2>\n')

	pagehtml.write('<table>\n<tr>\n')#debut du tableau qui englobe tout

	#prev aujourd'hui
	pagehtml.write("<td>\n<table>\n")#table qui contient info 1 jour
	pagehtml.write("<tr>\n")
	pagehtml.write("<td>\n")
	pagehtml.write("<table>\n")
	pagehtml.write("<tr>\n<td>Maintenant</td></tr>\n")
	pagehtml.write("<tr>\n<td>\n")
	pagehtml.write('<table>\n<tr>\n')
	pagehtml.write("<td>{}°\n".format(condition["temp"]))
	pagehtml.write("</td>\n")
	pagehtml.write('<td><img src="../img/meteo/{}.png"/></td>\n'.format(condition["code"]))
	pagehtml.write('</tr>\n</table>\n')
	pagehtml.write("</td>\n</tr>\n</table>\n")
	pagehtml.write("</td>\n")
	pagehtml.write('<td><div class="separator"></div></td>\n')#contien le separator
	pagehtml.write("</tr>\n")
	pagehtml.write("</table>\n")
	
	while i<=5:
		pagehtml.write("<td>\n<table>\n")#table qui contient info 1 jour
		pagehtml.write("<tr>\n")
		pagehtml.write("<td>\n")
		pagehtml.write("<table>\n")
		pagehtml.write('<tr>\n<td>{}</td></tr>\n'.format(getDay(forecast[i]["day"])))
		pagehtml.write("<tr>\n<td>\n")
		pagehtml.write('<table>\n<tr>\n')
		pagehtml.write("<td>\n")
		pagehtml.write("<table>\n<tr>\n")
		pagehtml.write('<td>{}°</td>'.format(forecast[i]["high"]))
		pagehtml.write('</tr>\n<tr>\n')
		pagehtml.write('<td><b>{}°</b></td>'.format(forecast[i]["low"]))
		pagehtml.write("</tr>\n</table>\n")
		pagehtml.write("</td>\n")
		pagehtml.write('<td><img src="../img/meteo/{}.png"/></td>\n'.format(forecast[i]["code"]))
		pagehtml.write('</tr>\n</table>\n')
		pagehtml.write("</td>\n</tr>\n</table>\n")
		pagehtml.write("</td>\n")
		if i ==5:
			pagehtml.write("<td></td>\n")
		else:
			pagehtml.write('<td><div class="separator"></div></td>\n')#contien le separator

		pagehtml.write("</tr>\n")
		pagehtml.write("</table>\n")

		i+=1

	pagehtml.write("</td>\n</tr>\n")
	pagehtml.write('</table>\n')
	pagehtml.write('</div>\n')

	######################################code pour le detail du jour
	pagehtml.write('<div id="details"> <h2> Détails</h2>\n')
	pagehtml.write("<table>\n")
	pagehtml.write('<tr>\n<td>Température ressentie</td> <td><b>{}°</b></td> <td>Humidité</td> <td><b>{} %</b></td>\n</tr>\n'.format(wind["chill"], atmospher["humidity"]))
	pagehtml.write('<tr>\n<td>Vent</td> <td><b>{} km/h</b></td> <td>Direction</td> <td><b>{}</b></td>\n</tr>\n'.format(wind["speed"],wind["direction"]))
	pagehtml.write('<tr>\n<td>Visibilité</td> <td><b>{} km</b></td> <td>Pression</td> <td><b>{} mBar</b></td>\n</tr>\n'.format(atmospher["visibility"],atmospher["pressure"]))
	pagehtml.write('<tr>\n<td>Levé</td> <td><b>{}</b></td> <td>Couché</td> <td><b>{}</b></td>\n</tr>\n'.format(astronomy["sunrise"],astronomy["sunset"]))
	pagehtml.write("</table>\n")

	pagehtml.write('</div>\n')

	######################################ecriture de la vigilance crue de la seine
	pagehtml.write('<div id="crue"><h2>Seine</h2>')
	pagehtml.write('<table>\n<tr><td><div id="{}">{}</div></td></tr></table>\n'.format(alerte,getDescription(alerte),dateMaj))
	pagehtml.write("</div>\n")#div fin crue

	pagehtml.write("</div>\n")#div fin meteo

	#pour forecast, les indices du dico sont hight,code,low,date,text,day
	#changer la couleur du texte des données et pas des textes de précisions (tp0, humidité ...)
