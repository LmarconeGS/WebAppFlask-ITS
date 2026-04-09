#ALL'INTERNO DI QUESTO FILE ANDREMO A DEFINIRE LE ROUTE DEL PROGETTO

from flask import render_template
import random

def init_app(app):

    #struttura base di una route
    @app.route("/")
    def home():
        #genera un numero intero random tra 1 e 100
        numero = random.randint(1, 100)
        #render_template prende i template dalla cartella templates se il file html si trova in una sottocartella va scritto nel percorso es. sottocartella/home.html
        return render_template("home.html", numero=numero)
    
    @app.route("/prova")
    def prova():
        #richiamiamo un altro template ma che estende lo stesso file base.html
        return render_template("home2.html")