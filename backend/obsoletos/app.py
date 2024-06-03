from flask import Flask
from flask_cors import CORS
""" from config import config """
# importo desde config el archivo el diccionario config que está dentro

# Routes
""" from routes import inventary
from routes import Barbershop """

app = Flask(__name__)

# Aca le digo que permite hacerle peticiones HTTP desde el servidor del fronted Vue
CORS(app, resources={"*": {"origins": "http://localhost:3000"}})


def page_not_found(error):
    return "<h1>Not found page</h1>", 404



# Aca le digo que la configuración va avenir desde unn objeto (copnfig)
if __name__ == '__main__':
    app.config["DEBUG"] = True

    # Blueprints
    app.register_blueprint(Barber.main, url_prefix='/api/barbers')
    app.register_blueprint(Barbershop.main, url_prefix='/api/barbershops')

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()