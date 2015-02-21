#! /usr/bin/python2.7
# -*-coding:Utf-8 -*

from bs4 import BeautifulSoup
import subprocess

def recupAlerte():
	niveauAlerte = ""
	dateMaj = ""

	url = 'http://www.vigicrues.gouv.fr/rss/?codeTron=IF3'
	res, error = subprocess.Popen(['curl',url], stdout = subprocess.PIPE).communicate()

	if error is None:
		soup = BeautifulSoup(res)
		title = soup.find_all('title')[2]
		title = str(title)
		title = title.split(' ')[3]
		niveauAlerte = title.replace('</title>','')

		date = soup.find_all('pubdate')[0]
		date = str(date)
		dateMaj = date.replace('<pubdate>','')
		dateMaj = date.replace('</pubdate>','')
		return niveauAlerte, dateMaj

	else:
		print("Erreur de récupération de l'alerte crue")
		return None, None

def getDescription(niveauAlerte):
	return{
	"Rouge":"Risque de crue majeure. Menace directe et généralisée de la sécurité des personnes et des biens.",
	"Orange":"Risque de crue génératrice de débordements importants susceptibles d’avoir un impact significatif sur la vie collective et la sécurité des biens et des personnes.",
	"Jaune":"Risque de crue ou de montée rapide des eaux n'entraînant pas de dommages significatifs, mais nécessitant une vigilance particulière dans le cas d'activités saisonnières et/ou exposées.",
	"Vert":"Pas de vigilance particulière requise"
	}[niveauAlerte]

if __name__ == '__main__':
	alerte, dateMaj = recupAlerte()
	if alerte is not None and dateMaj is not None:
		print('{} {} {}'.format(alerte,getDescription(alerte),dateMaj))

