import os
import xml.etree.ElementTree as ET

def getFichier():
	"""Recupère le fichier de vigilance de crue de la seine"""
	res = os.system('curl http://www.vigicrues.gouv.fr/rss/?codeTron=IF3 >>crue.xml')
	return res # retourne le code d'erreur de la commande

def ecritHtml(dateMaj,niveauAlerte)

def recupAlerte():
	itemTrouve = False
	niveauAlerte = ""
	dateMaj = ""
	res = getFichier()
	if res == 0:

		tree = ET.parse("crue.xml")
		root = tree.getroot()
		for elem in root.getiterator():
			print(elem.tag)
			print(elem.text)
			if(elem.tag == "item"):
				itemTrouve = True

			elif(elem.tag == "pubDate"):
				dateMaj = elem.text

			if(itemTrouve):
				if(elem.tag == "title"):
					niveauAlerte = elem.text




		print("------------------------------------")
		print("niveau alerte {}".format(niveauAlerte))
		print("date maj {}".format(dateMaj))
	else:
		print("Erreur de récupération du fichier crue.xml depuis le web")