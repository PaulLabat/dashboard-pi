#! /usr/bin/python2.7
# -*-coding:Utf-8 -*

from time import sleep
import sys, os
from meteo import ecritMeteo
from crue import ecritCrue
import html
from poubelles import ecritPoubelles
from date import ecritDate
from rer import ecritTraficRer
from alertesMeteo import ecritVigilance

if __name__ == '__main__':
	#appel du programme principal
	woeidAthis = "22144181"
	woeidMaucloup = "595357"
	athis = "Athis-Mons"
	maucloup = "Maucloup"
	crueCodeSeine = "IF3"
	seine = "Seine"
	vienne = "Vienne"
	crueCodeVienne = "VT6"

	while True:
		pagehtml = open("index.html", "w") #fichier qui contient le code
		html.ecritDebutHtml(pagehtml)
		ecritMeteo(pagehtml, woeidAthis, athis)
		ecritVigilance(91,pagehtml)
		ecritCrue(pagehtml,crueCodeSeine, seine)
		ecritTraficRer(pagehtml)
		ecritPoubelles(pagehtml)
		ecritDate(pagehtml)
		html.ecritFinHtml(pagehtml)
		pagehtml.close()

		pagehtml = open("maucloup.html", "w") #fichier qui contient le code
		html.ecritDebutHtml(pagehtml)
		ecritMeteo(pagehtml, woeidMaucloup, maucloup)
		ecritVigilance(87,pagehtml)
		ecritCrue(pagehtml,crueCodeVienne, vienne)
		ecritDate(pagehtml)
		html.ecritFinHtml(pagehtml)
		pagehtml.close()

		print("sleep\n")
		sleep(3600)#rafraichissement toutes les heures
