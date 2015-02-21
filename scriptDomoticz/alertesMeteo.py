#! /usr/bin/python2.7
# -*-coding:Utf-8 -*

import subprocess
import json

def getVigilance():
	vigilanceColor = None
	vigilanceRisk = None
	
	url = 'http://api.domogeek.fr/vigilance/91/all'
	res, error = subprocess.Popen(['curl',url], stdout = subprocess.PIPE).communicate()
	if error is None:
		try:
			data = json.loads(res)
			vigilanceColor = data['vigilancecolor'].encode('utf-8')
			vigilanceRisk = data['vigilancerisk'].encode('utf-8')
		except (ValueError, KeyError, TypeError):
			print("JSON format error")

	return vigilanceColor, vigilanceRisk

if __name__ == '__main__':
	vigilanceColor, vigilanceRisk = getVigilance()
	if vigilanceRisk is not None and vigilanceColor is not None:
		print("{} {} {}".format(vigilanceColor,vigilanceColor, vigilanceRisk))

