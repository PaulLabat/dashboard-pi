# -*-coding:Utf-8 -*
from os import system

def getMeteo():
	return """<div id="cont_MzgxODV8NXw0fDR8NHwwMDAwMDB8MXxGRkZGRkZ8Y3wx"><div id="spa_MzgxODV8NXw0fDR8NHwwMDAwMDB8MXxGRkZGRkZ8Y3wx"><a id="a_MzgxODV8NXw0fDR8NHwwMDAwMDB8MXxGRkZGRkZ8Y3wx" href="http://www.meteocity.com/france/grenoble_v38185/" target="_blank" style="color:#000;text-decoration:none;">Météo Grenoble</a></div><script type="text/javascript" src="http://widget.meteocity.com/js/MzgxODV8NXw0fDR8NHwwMDAwMDB8MXxGRkZGRkZ8Y3wx"></script></div> """

def ecritMeteo(pagehtml):
	#code pour meteo
		pagehtml.write('<div id="meteo">{}</div>\n'.format(getMeteo()))

def getMeteoYahoo():
	return system('curl "http://weather.yahooapis.com/forecastrss?w=22144181&u=c" >> orly.xml')