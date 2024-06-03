from flask import Flask, jsonify, request
from flask_cors import CORS
from backend.mesh_tree.buildTree import build_tree
from backend.mesh_tree.createList import createList
from pymongo import MongoClient
from bson import ObjectId
from backend.client_detail.formater_client_detail import levels_shovels

print(levels_shovels)

mongoClient = MongoClient("localhost",27017)
db = mongoClient.monitorTree

app = Flask(__name__)

@app.route('/mesh', methods=['GET'])
def getTree():
    try:
        print("solicitud construyendo árbol mesh")
        tree = build_tree(createList())
        print("solicitud resuelta")
        return jsonify(tree)  
    except Exception as e:
        print("no se logro procesar solicitud",e)
        return jsonify(e) 


#---------inventary------------
#--create--
""" @app.route('/inventary', methods=['GET'])
def createDevice():
  print("obteniendo dispositivos")
  print(request.json)
  id = db.insert({
    'inventary_ip': request.json['inventary_ip'],
    'hostname': request.json['hostname'],
    'parent_default': request.json['parent_default']
  })
  return jsonify(str(ObjectId(id))) """

#--read--
@app.route('/inventary', methods=['GET'])
def getDevices():
    print("obteniendo dispositivos")
    try:
        devices = []
        for doc in db.inventary.find():
            devices.append({
                '_id': str(ObjectId(doc['_id'])),
                'inventary_ip': doc['inventary_ip'],
                'hostname': doc['hostname'],
                'parent_default': doc['parent_default']
            })
        return jsonify(devices)
    except Exception as e:
        print("no se logro procesar solicitud",e)
        return jsonify(e) 
    



#--read--
@app.route('/inventary/<id>', methods=['GET'])
def getDevice(id):
  device = db.find_one({'_id': ObjectId(id)})
  print(device)
  return jsonify({
      '_id': str(ObjectId(device['_id'])),
      'hostname': device['hostname'],
      'inventary_ip': device['inventary_ip'],
      'parent_default': device['parent_default']
  })

#--update
@app.route('/inventary/<id>', methods=['PUT'])
def updateUser(id):
  print(request.json)
  db.update_one({'_id': ObjectId(id)}, {"$set": {
    'hostname': request.json['hostname'],
    'parent_default': request.json['parent_default'],
    'inventary_ip': request.json['inventary_ip']
  }})
  return jsonify({'message': 'Dispositivo actualizado'})

#--delete
@app.route('/inventary/<id>', methods=['DELETE'])
def deleteUser(id):
  db.delete_one({'_id': ObjectId(id)})
  return jsonify({'message': 'Dispositivo eliminado'})

#-----niveles de señal de clientes------------------------->>>

@app.route('/clients-levels', methods=['GET'])
def getSignals():
    print("Obteniendo niveles de señal de los clientes")
    try:
        print("solicitud resuelta") 
        return jsonify(levels_shovels)
    except Exception as e:
        print("No se logro procesar solicitud",e)
        return jsonify(e) 


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