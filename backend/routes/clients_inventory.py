from flask import Flask, jsonify, request, Blueprint
from pymongo import MongoClient
from bson import ObjectId
from pprint import pprint

mongoClient = MongoClient("localhost",27017)
db = mongoClient.monitorTree


clients_inventory = Blueprint('clients_inventory', __name__)

#---------clients_inventory------------
#--create--
@clients_inventory.route('/clients_inventory', methods=['POST'])
def createDevice():
  try:
    print("Agregando nuevo cliente")
    print(request.json)
    client = request.json["client"]
    db.clients_inventory.insert_one({
        'inventory_ip': client['inventory_ip'],
        'hostname': client['hostname'],
        'service': client['service'],
        'tag': client['tag'],
        'equipment': client['equipment']
    })
    print('Se agregó correctamente')
    return jsonify({"data":"Se logró agregar cliente"})
  except Exception as e:
        print("No se logró agregar cliente",e)
        return jsonify({"data":"*No se logró agregar cliente"})

#--read all--
@clients_inventory.route('/clients_inventory', methods=['GET'])
def getDevices():
    print("Obteniendo dispositivos")
    try:
        devices = []
        for doc in db.clients_inventory.find():
            devices.append({
                'id': str(ObjectId(doc['_id'])),
                'inventory_ip': doc['inventory_ip'],
                'hostname': doc['hostname'],
                'service': doc['service'],
                'tag': doc['tag'],
                'equipment': doc['equipment']
            })
    except Exception as e:
       print('Error al obtener los clientes', e)
       return jsonify({"data":"No se logró obtener los clientes"})
    else:
       print("Se obtuvieron los clientes correctamente")
       return jsonify(devices)
    
    

#--read--------------------------------------------------->
@clients_inventory.route('/clients_inventory/<id>', methods=['GET'])
def getDevice(id):
  device = db.clients_inventory.find_one({'_id': ObjectId(id)})
  print(device)
  return jsonify({
    '_id': str(ObjectId(device['_id'])),
    'inventory_ip': device['inventory_ip'],
    'hostname': device['hostname'],
    'parent_default': device['parent_default'],
    'service': device['service'],
    'tag': device['tag'],
    'equipment': device['equipment']
  })

#--read----Aqui leo el cliente con la ip-------------->
@clients_inventory.route('/clients_inventory/ip/<ip>', methods=['GET'])
def getDeviceIP(ip):
    try:
        print("consultando por la ip", ip)
        res = db.clients_inventory.find_one({'inventory_ip': ip})
        print("Respuesta", res)
        if res is None:
           print("Dispositivo no registrado")
           return jsonify({"data":"Dispositivo no registrado"})
        else:
            print("Dispotivo obtenido correctamente")
            return jsonify({
                '_id': str(ObjectId(res['_id'])),
                'inventory_ip': res['inventory_ip'],
                'hostname': res['hostname'],
                'parent_default': res['parent_default'],
                'service': res['service'],
                'tag': res['tag'],
                'equipment': res['equipment']
            })
    except Exception as e:
       print('error al obtener el cliente', e)
       return jsonify({"data":"*No se logró obtener cliente"})



#--update-------------------------------------------------->
@clients_inventory.route('/clients_inventory/<id>', methods=['PUT'])
def updateClient(id):
    try:
        print("editando cliente", id)
        print(request.json)
        client = request.json["client"]
        #db.update_one({'_id': ObjectId(id)}, {"$set": request.json})
        
        db.clients_inventory.update_one({'_id': ObjectId(id)}, {"$set": {
                'inventory_ip': client['inventory_ip'],
                'hostname': client['hostname'],
                'parent_default': client['parent_default'],
                'service': client['service'],
                'tag': client['tag'],
                'equipment': client['equipment']
        }})
        return jsonify({"data":"*Si se logró agregar cliente"})
    except Exception as e:
       print('error al actualizar el cliente', e)
       return jsonify({"data":"*No se logró agregar cliente"})

#--delete
@clients_inventory.route('/clients_inventory/<id>', methods=['DELETE'])
def deleteUser(id):
  db.clients_inventory.delete_one({'_id': ObjectId(id)})
  return jsonify({'message': 'Dispositivo eliminado'})
