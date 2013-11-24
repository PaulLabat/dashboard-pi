# -*-coding:Utf-8 -*
from icalendar import Calendar
from date import compareDate

def getNextEvent(fichier):
	nbCal = 1
	fiveDay = dict()
	ical = open(fichier,'rb')
	cal = Calendar.from_ical(ical.read())
	ical.close()
	for component in cal.walk():
		if component.name == "VEVENT" and nbCal <= 5:
			if compareDate(str(component.get("dtstart").dt.date())): #force la recuperation des 5 prochains evenements
				day = dict()
				day["summary"] = component.get('summary').encode("utf-8")#recupere la chaine de caractere et l'encode en utf-8
				day["dstart"] = str(component.get('dtstart').dt.date()) # recupere la date, la transforme de datetime.datetime puis la passe en string avec le str et le .date()
				day["tstart"] = str(component.get('dtstart').dt.time())#recupere l'heure
				day["dend"] = str(component.get('dtend').dt.date())
				day["tend"] = str(component.get('dtend').dt.time())
				day["location"] = component.get('location').encode("utf-8")
				fiveDay[nbCal] = day
				nbCal +=1

	return fiveDay

def ecritCalendar(pagehtml):
	fiveDay = getNextEvent('../ics/paul.ics')
	pagehtml.write('<div id="calendar">\n<div id="titrecalendar">Prochains rendez-vous</div><br>\n')
	for elem in fiveDay.keys():
		pagehtml.write("{} le <b>{}</b> à {} jusqu'au <b>{}</b> à {} lieu : {}<br>\n".format(fiveDay[elem]["summary"], fiveDay[elem]["dstart"],fiveDay[elem]["tstart"], fiveDay[elem]["dend"],fiveDay[elem]["tend"], fiveDay[elem]["location"]))
	pagehtml.write("</div>")

#mettre la date au format europeen et non americain