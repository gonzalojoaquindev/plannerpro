from flask import Flask, jsonify, request
from flask_cors import CORS

from routes.accounts import accounts
from routes.categories import categories
from routes.subcategories import subcategories
from routes.benefited import benefited
from routes.transactions import transactions


app = Flask(__name__)


app.register_blueprint(accounts)
app.register_blueprint(categories)
app.register_blueprint(subcategories)
app.register_blueprint(benefited)
app.register_blueprint(transactions)


""" @app.route('/mesh/wlc', methods=['GET'])
def getConection():
    try:
        print("Conectando a WLC-----")
        data = build_tree(createList())
        return jsonify({"msg":"Se obtuvieron los datos correctamente de WLC","data":data})  
    except Exception as e:
        print("No se logró ingresar a WLC",e)
        return jsonify({"msg":"No se logró ingresar a WLC", "detail": e})
    else:
        print("Solicitud resuelta----") """
        
"""    
@app.route('/mesh/db', methods=['GET'])   
def conectionDB():
    try:
        print("intentando acceder a base de datos-------------")
        return jsonify({"msg":"conexion existosa"})
    except Exception as e:
        print(e)
        return jsonify({"msg":"No se logró ingresar a base de datos","detail": e})
""" 





#--read--


#-----niveles de señal de clientes------------------------->>>

""" @app.route('/clients-levels', methods=['GET'])
def getSignals():
    print("Obteniendo detalles de los clientes")
    try:
        print("solicitud resuelta")
       
        return jsonify(levels_shovels)
    except Exception as e:
        print("No se logro procesar solicitud",e)
        return jsonify(e)  """


# Aca le digo que permite hacerle peticiones HTTP desde el servidor del fronted Vue
CORS(app, resources={"*": {"origins": "http://localhost:5173"}})


def page_not_found(error):
    return "<h1>Not found page</h1>", 404



# Aca le digo que la configuración va avenir desde unn objeto (copnfig)
if __name__ == '__main__':
    app.config["DEBUG"] = True
    # Error handlers
    app.register_error_handler(404, page_not_found)
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)