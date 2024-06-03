from flask import Flask, jsonify
from flask_cors import CORS
from backend.mesh_tree.buildTree import build_tree
from backend.mesh_tree.createList import createList



app = Flask(__name__)

@app.route('/mesh', methods=['GET'])
def getTree():
    """  try:
        aps = get_aps_from_wlc()
        return jsonify( {"status": "Se obtuvieron correctamente los ap desde WLC",
                "datos": aps
                })
    except Exception as e:
        print(e) """
    try:
        print("solicitud construyendo árbol mesh")
        tree = build_tree(createList())
        print("solicitud resuelta")
        return jsonify(tree)  
    except Exception as e:
        print("no se logro procesar solicitud",e)
        return jsonify(e) 

""" @app.route('/conect_to_wlc', methods=['GET'])
def conect_to_wlc():
    return jsonify("Conectando a WLC respuesta") """
@app.route('/ap', methods=['GET'])
def ap():
    return jsonify("Conexón exitosa")
""" def variosMensajes():
    

def mensaje1():
    return jsonify("mensaje 1") """


# Aca le digo que permite hacerle peticiones HTTP desde el servidor del fronted Vue
CORS(app, resources={"*": {"origins": "http://10.16.248.52:5173"}})


def page_not_found(error):
    return "<h1>Not found page</h1>", 404



# Aca le digo que la configuración va avenir desde unn objeto (copnfig)
if __name__ == '__main__':
    app.config["DEBUG"] = True
    # Error handlers
    app.register_error_handler(404, page_not_found)
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)