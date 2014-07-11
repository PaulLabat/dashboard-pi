# -*-coding:Utf-8 -*
import urllib2
from bs4 import BeautifulSoup


def getPoubelles():
	dico = dict()
	i=1
	try:
		url = urllib2.urlopen('http://www.portesessonne.fr/Vivre-et-entreprendre/Dechets/Quand-sortir-mes-poubelles', "BuildingType=1&LoadStreetsUrl=%2Fsdform%2Fload_street&City=2&Street=219&SubitRequestSmallButton=")
	except IOError:
		print("Impossible de récupérer les données pour les poubelles.")
	else:
		soup = BeautifulSoup(url.read())
		for td in soup.find_all('td'):
			dico[i] = td.string.encode("utf-8")
			i = i+1


	return dico

def ecritPoubelles(pagehtml):
	dico = getPoubelles()
	i=1
	pagehtml.write('<h2 class="sub-header">Calendrier des poubelles</h2><table class="table table-striped" style="width:720px;">\n')
	for elm in dico.values():
		if(i%2==0):
			pagehtml.write('<td><b>{}</b></td>\n</tr>\n'.format(elm))
		else:
			pagehtml.write('<tr>\n<td>{}</td>\n'.format(elm))

		i = i+1

	pagehtml.write('</table>\n')
