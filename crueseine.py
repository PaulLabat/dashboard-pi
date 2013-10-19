import os
import xml.etree.ElementTree as ET

def getFichier():
	"""Recupère le fichier de vigilance de crue de la seine"""
	res = os.system('curl http://www.vigicrues.gouv.fr/rss/?codeTron=IF3 >>crue.xml')
	return res # retourne le code d'erreur de la commande
	

def recupAlerte():
	itemTrouve = False
	niveauAlerte = ""
	dateMaj = ""
	res = getFichier()
	if res == 0:

		tree = ET.parse("crue.xml")
		root = tree.getroot()
		for elem in root.getiterator():
			if(elem.tag == "item"):
				itemTrouve = True

			elif(elem.tag == "pubDate"):
				dateMaj = elem.text

			if(itemTrouve):
				if(elem.tag == "title"):
					niveauAlerte = elem.text

		niveauAlerte = niveauAlerte.split()[3] #recup le dernier element qui est la couleur de l'alerte

	else:
		print("Erreur de récupération du fichier crue.xml depuis le web")

	return niveauAlerte, dateMaj


def getDescription(niveauAlerte):
	return{
	"Rouge":"Risque de crue majeure. Menace directe et généralisée de la sécurité des personnes et des biens.",
	"Orange":"Risque de crue génératrice de débordements importants susceptibles d’avoir un impact significatif sur la vie collective et la sécurité des biens et des personnes.",
	"Jaune":"Risque de crue ou de montée rapide des eaux n'entraînant pas de dommages significatifs, mais nécessitant une vigilance particulière dans le cas d'activités saisonnières et/ou exposées.",
	"Vert":"Pas de vigilance particulière requise"
	}[niveauAlerte]



def ecritCrueSeine(pageHtml):
	niveauAlerte,dateMaj = recupAlerte()


	pageHtml.write("""\n<div id="crue"> <h3> Info crues de la Seine</h3>\n""")
	pageHtml.write("""<div id="alerte">Niveau de l'alerte : <img src="{}.jpg" alt="{}" /> {}</div>\n""".format(niveauAlerte, niveauAlerte, niveauAlerte))
	
	pageHtml.write("""<div id="description"> {}</div>\n""".format(getDescription(niveauAlerte)))
	pageHtml.write("""<div id="dateMaj"> Dernière mise à jour : {} </div>\n""".format(dateMaj))
	pageHtml.write("</div>\n")