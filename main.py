#! /usr/bin/python3.2
# -*-coding:Utf-8 -*

from time import sleep,localtime
import sys


def getTime():
	return localtime()

def ecritDebutHtml(pagehtml):
	pagehtml.write("""
<!DOCTYPE html>\n
<html>\n
    <head>\n
        <meta charset="utf-8" />\n
        <link rel="stylesheet" type="text/css" href="style.css" />\n
        <title>Station météo</title>\n
    </head>\n
 
    <body>\n
    <script src="script.js"></script>\n
    
		""")

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


def getMeteo():
	return """<div id="cont_MzgxODV8NXw0fDR8NHwwMDAwMDB8MXxGRkZGRkZ8Y3wx"><div id="spa_MzgxODV8NXw0fDR8NHwwMDAwMDB8MXxGRkZGRkZ8Y3wx"><a id="a_MzgxODV8NXw0fDR8NHwwMDAwMDB8MXxGRkZGRkZ8Y3wx" href="http://www.meteocity.com/france/grenoble_v38185/" target="_blank" style="color:#000;text-decoration:none;">Météo Grenoble</a></div><script type="text/javascript" src="http://widget.meteocity.com/js/MzgxODV8NXw0fDR8NHwwMDAwMDB8MXxGRkZGRkZ8Y3wx"></script></div> """


def ecritFinHtml(pagehtml):
	pagehtml.write("\n</body>\n </html>")


if __name__ == '__main__':
	#appel du programme principal
	if len(sys.argv) == 2 and sys.argv[1] == "runserver": #si ya un argument on execute le code
		print("runserver")
		while True:
			pagehtml = open("index.html", "w") #fichier qui contient le code
			time = getTime()
			ecritDebutHtml(pagehtml)
			#code pour date
			pagehtml.write('<div id="horloge"><div id="horloge_heure"> {}:{}</div>\n'.format(time.tm_hour, time.tm_min))
			pagehtml.write("""<div id="horloge_date">\n
			 {} {} {} {}</div>""".format(getDay(time.tm_wday),time.tm_mday,getMonth(time.tm_mon),time.tm_year))
			pagehtml.write('</div>\n')#div de horloge

			#code pour meteo
			pagehtml.write('<div id="meteo">{}</div>'.format(getMeteo()))

			ecritFinHtml(pagehtml)
			pagehtml.close()
			sleep(10)



	else:
		print("Mauvais argument ou pas d'argument. Voir l'aide")
	
		
#fonction a utiliser
# mettre en pause un soft time.sleep(temps);
#modifier le script de rafraichissement auto
# localtime = http://www.jchr.be/python/modules.htm
#pour la meteo recup la page http://france.meteofrance.com/france/meteo?PREVISIONS_PORTLET.path=previsionsville/381850
#puis chercher le code qui va bien
#rajouter les grèves sncf et ratp
#rajouter un interpréteur de commande shell
#un thread pour rafraichir heure :toutes les minutes
#un thread pour rafraichir date : 1fois par jour
#thread pour météo : toute les 4h
#thread pour le reste