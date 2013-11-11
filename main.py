#! /usr/bin/python2.7
# -*-coding:Utf-8 -*

from time import sleep
import sys, os, help
import help
from meteo import ecritMeteo
import html
from poubelles import ecritPoubelles


if __name__ == '__main__':
	#appel du programme principal
	if len(sys.argv) == 2 and sys.argv[1] == "runserver": #si ya un argument on execute le code
		print("runserver")
		while True:
			os.system("rm crue.xml") #supp le vieux fichier xml
			os.system("rm orly.xml")
			pagehtml = open("index.html", "w") #fichier qui contient le code
			html.ecritDebutHtml(pagehtml)

			ecritMeteo(pagehtml)
			ecritPoubelles(pagehtml)

			html.ecritFinHtml(pagehtml)
			pagehtml.close()
			print("sleep\n")
			sleep(60)#rafraichissement toutes les minutes, a modifier par 60


	elif len(sys.argv) == 2 and sys.argv[1] == "--help":
		help.help()

	else:
		print("Voir './main.py --help'")
