# -*-coding:Utf-8 -*
from bs4 import BeautifulSoup
import subprocess

def recupAlerte(code):
	niveauAlerte = ""
	dateMaj = ""

	url = 'http://www.vigicrues.gouv.fr/rss/?codeTron='+str(code)
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

def ecritCrue(pagehtml, code, fleuve):
	alerte, dateMaj = recupAlerte(code)
	if alerte is not None and dateMaj is not None:
		pagehtml.write('<h3 class="sub-header">'+fleuve+'</h3>')
		pagehtml.write('<span class="{}">{}</span>\n<br><span style="font-size:10px;">{}</span>\n'.format(alerte,getDescription(alerte),dateMaj))
