#FILE CORE PER IMPORTARE LE ROUTE E LE VARIABILI DI SISTEMA

#import librerie
from flask import Flask
from dotenv import load_dotenv

#funzione per creare l'app
def create_app():

    #carica il file .env
    load_dotenv() 
    
    #definisce app
    app = Flask(__name__)

    #import routes
    from . import routes
    routes.init_app(app)

    return app