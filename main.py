#! /usr/bin/python3.2
# -*-coding:Utf-8 -*

from time import sleep
import sys, os, help
import help
from date import ecritDate
from meteo import ecritMeteo
import html
from crueseine import ecritCrueSeine


if __name__ == '__main__':
	#appel du programme principal
	if len(sys.argv) == 2 and sys.argv[1] == "runserver": #si ya un argument on execute le code
		print("runserver")
		while True:
			os.system("rm crue.xml") #supp le vieux fichier xml
			pagehtml = open("index.html", "w") #fichier qui contient le code
			html.ecritDebutHtml(pagehtml)

			ecritDate(pagehtml)
			ecritMeteo(pagehtml)

			ecritCrueSeine(pagehtml)

			html.ecritFinHtml(pagehtml)
			pagehtml.close()
			
			sleep(2)#rafraichissement toutes les minutes


	elif len(sys.argv) == 2 and sys.argv[1] == "--help":
		help.help()

	else:
		print("Voir './main.py --help'")
	