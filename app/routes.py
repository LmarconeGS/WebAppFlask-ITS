#ALL'INTERNO DI QUESTO FILE ANDREMO A DEFINIRE LE ROUTE DEL PROGETTO

from flask import render_template

def init_app(app):

    #struttura base di una route
    @app.route("/")
    def home():
        #render_template prende i tempalte dalla cartella templates se il file html si trova in una sottocartella va scritto nel percorso es. sottocartella/home.html
        return render_template("home.html")