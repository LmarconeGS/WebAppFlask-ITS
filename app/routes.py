#ALL'INTERNO DI QUESTO FILE ANDREMO A DEFINIRE LE ROUTE DEL PROGETTO

def init_app(app):

    #struttura base di una route
    @app.route("/")
    def home():
        return "Prova 123"