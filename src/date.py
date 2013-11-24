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
	1:"Janvier",
	2:"Févirer",
	3:"Mars",
	4:"Avril",
	5:"Mai",
	6:"Juin",
	7:'Juiller',
	8:"Août",
	9:"Septembre",
	10:"Octobre",
	11:"Novembre",
	12:"Decembre"
	}[mois]

def returnDate():
	time = getTime()
	return getDay(time.tm_wday),time.tm_mday,getMonth(time.tm_mon),time.tm_year, time.tm_hour, time.tm_min