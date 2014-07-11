# -*-coding:Utf-8 -*
def ecritDebutHtml(pagehtml):
	pagehtml.write("""
<!DOCTYPE html>\n
<html lang="fr">\n
  <head>\n
    <meta charset="utf-8">\n
    <meta name="viewport" content="width=device-width, initial-scale=1">\n
    <title>Dashboard</title>\n
    <!-- Bootstrap core CSS -->\n
    <link href="../bootstrap/css/bootstrap.min.css" rel="stylesheet">\n
    <!-- Custom styles for this template -->\n
    <link href="../css/dashboard.css" rel="stylesheet">\n
    <link rel="stylesheet" type="text/css" href="../css/style.css" />\n
  </head>\n

  <body>\n

    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">\n
      <div class="container-fluid">\n
        <div class="navbar-header">\n
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\n
            <span class="sr-only">Toggle navigation</span>\n
            <span class="icon-bar"></span>\n
            <span class="icon-bar"></span>\n
            <span class="icon-bar"></span>\n
          </button>\n
          <a class="navbar-brand" href="#">Dashboard</a>\n
        </div>\n
        <div class="navbar-collapse collapse">\n
          <ul class="nav navbar-nav navbar-right">\n
            <li><a href="index.html">Athis-Mons</a></li>\n
            <li><a href="maucloup.html">Maucloup</a></li>\n
          </ul>\n
        </div>\n
      </div>\n
    </div>\n

    <div class="container-fluid"><!--main part-->\n """)




def ecritFinHtml(pagehtml):
	pagehtml.write("""\n</div>\n
    <script src="../javascript/jquery.min.js"></script>\n
    <script src="../bootstrap/js/bootstrap.min.js"></script>\n
  </body>\n
</html>\n
""")
