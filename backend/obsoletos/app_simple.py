from flask import Flask, jsonify
from flask_cors import CORS
from backend.obsoletos.buildTree import build_tree
from backend.obsoletos.createList import combined_list
from backend.obsoletos.conectionWLC import get_data_from_wlc


# Routes
""" from routes import inventary
from routes import Barbershop """

app = Flask(__name__)

@app.route('/mesh', methods=['GET'])
def getTree():
    get_data_from_wlc()
    tree = build_tree(combined_list)
    print("obteniendo arbol mesh")
    
    return jsonify(tree)

# Aca le digo que permite hacerle peticiones HTTP desde el servidor del fronted Vue
CORS(app, resources={"*": {"origins": "http://localhost:5173"}})


def page_not_found(error):
    return "<h1>Not found page</h1>", 404



# Aca le digo que la configuración va avenir desde unn objeto (copnfig)
if __name__ == '__main__':
    app.config["DEBUG"] = True
    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run(debug=True)