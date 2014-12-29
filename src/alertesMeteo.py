# -*-coding:Utf-8 -*

import subprocess
from date import ecritDate
import json

def getVigilance(departement):
	vigilanceColor = None
	vigilanceRisk = None
	
	url = 'http://api.domogeek.fr/vigilance/'+str(departement)+'/all'
	res, error = subprocess.Popen(['curl',url], stdout = subprocess.PIPE).communicate()
	if error is None:
		try:
			data = json.loads(res)
			vigilanceColor = data['vigilancecolor'].encode('utf-8')
			vigilanceRisk = data['vigilancerisk'].encode('utf-8')
		except (ValueError, KeyError, TypeError):
			print("JSON format error")

	return vigilanceColor, vigilanceRisk

def ecritVigilance(departement, html):
	url = "http://vigilance.meteofrance.com/Bulletin_sans.html?a=dept"+str(departement)+"&b=2&c="
	vigilanceColor, vigilanceRisk = getVigilance(departement)
	if vigilanceRisk is not None and vigilanceColor is not None:
		html.write('<h3 class="sub-header"><a href="{}">Vigilance météo</a></h3>\n'.format(url))
		html.write('<span class="{}">Vigilance : {}</span><br>Risque : {}<br>'.format(vigilanceColor,vigilanceColor, vigilanceRisk))
