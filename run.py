#FILE PER L'AVVIO DELL'APP
from app import create_app

app = create_app()

if __name__ == "__main__":
    #funzione per avviare il server Flask
    app.run()