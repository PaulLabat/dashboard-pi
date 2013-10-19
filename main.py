#! /usr/bin/python3.2
# -*-coding:Utf-8 -*

from time import sleep
import sys
import help
from date import ecritDate
from meteo import ecritMeteo
import html

if __name__ == '__main__':
	#appel du programme principal
	if len(sys.argv) == 2 and sys.argv[1] == "runserver": #si ya un argument on execute le code
		print("runserver")
		while True:
			pagehtml = open("index.html", "w") #fichier qui contient le code
			html.ecritDebutHtml(pagehtml)

			ecritDate(pagehtml)
			ecritMeteo(pagehtml)

			html.ecritFinHtml(pagehtml)
			pagehtml.close()
			sleep(60)#rafraichissement toutes les minutes

	elif len(sys.argv) == 2 and sys.argv[1] == "--help":
		help.help()

	else:
		print("Voir './main.py --help'")
	