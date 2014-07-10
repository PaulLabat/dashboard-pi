# -*-coding:Utf-8 -*
def ecritDebutHtml(pagehtml):
	pagehtml.write("""
<!DOCTYPE html>\n
<html>\n
    <head>\n
        <meta charset="utf-8" />\n
        <link rel="stylesheet" type="text/css" href="../css/style.css" />\n
         <link rel="stylesheet" type="text/css" href="../css/meteo.css" />\n
          <link rel="stylesheet" type="text/css" href="../css/crue.css" />\n
           <link rel="stylesheet" type="text/css" href="../css/poubelle.css" />\n
            <link rel="stylesheet" type="text/css" href="../css/calendrier.css" />\n
        <title>Station météo</title>\n
    </head>\n
 
    <body>\n
    <script src="../javascript/script.js"></script>\n
    <div id="menuMeteo" onCLick="Meteo();">Météo</div>\n <div id="menuPoubelle" onCLick="Poubelle();">Poubelle</div> \n """)




def ecritFinHtml(pagehtml):
	pagehtml.write("\n</body>\n </html>")
