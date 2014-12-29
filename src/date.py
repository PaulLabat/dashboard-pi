# -*-coding:Utf-8 -*
from time import localtime

def getTime():
	return localtime()

def getDay(day):
	return{
	0:"Lundi",
	1:"Mardi",
	2:"Mercredi",
	3:"Jeudi",
	4:"Vendredi",
	5:"Samedi",
	6:"Dimanche"

	}[day]

def getMonth(mois):
	return{
	1:"janvier",
	2:"février",
	3:"mars",
	4:"avril",
	5:"mai",
	6:"juin",
	7:'juillet',
	8:"août",
	9:"septembre",
	10:"octobre",
	11:"novembre",
	12:"décembre"
	}[mois]

def compareDate(date):
	dateSplit = date.split("-")
	time = getTime()
	egale = False
	if dateSplit[0] > str(time.tm_year):
		egale = True
	elif (dateSplit[0] == str(time.tm_year)) and (dateSplit[1] > str(time.tm_mon)):
		egale = True
	elif (dateSplit[0] == str(time.tm_year)) and (dateSplit[1] == str(time.tm_mon)) and (dateSplit[2] >= str(time.tm_mday)):
		egale = True

	return egale

def correctionMinute(min):
	if min < 10:
		return '0'+str(min)
	else:
		return min

def ecritDate(html):
	time = getTime()
	html.write('<br><br><br><div class="footer navbar-default navbar navbar-fixed-bottom">\n<div class="container">\n<span class="navbar-text">\n')
	html.write('Dernière récupération des données : {} {} {} {} à {}:{}'.format(getDay(time.tm_wday),time.tm_mday,getMonth(time.tm_mon),time.tm_year, time.tm_hour, correctionMinute(time.tm_min)))
	html.write('</span>\n</div>\n</div>\n')