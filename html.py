# -*-coding:Utf-8 -*
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
    <div id="menuMeteo" onCLick="Meteo();">Météo</div> <div id="menuPoubelle" onCLick="Poubelle();">Poubelle</div>
		""")




def ecritFinHtml(pagehtml):
	pagehtml.write("\n</body>\n </html>")