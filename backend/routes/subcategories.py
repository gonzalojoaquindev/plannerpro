from flask import Flask, jsonify, request, Blueprint
from db.db import mycursor
from db.db import db

print("iniciando subcategorias")

subcategories = Blueprint('subcategories', __name__)

#---------Subcategorias------------

#--create--
@subcategories.route('/subcategories', methods=['POST'])
def createcategory():
    print("crear cuenta")
    try:
        print("estoy dentro del bloque try")
        subcategory = request.json
        print(subcategory)
        print(subcategory["name"])
        sql = "INSERT INTO subcategories (category_id, color, icon, name, description) VALUES (%s, %s, %s, %s, %s)"
        val = (subcategory["category_id"], subcategory["color"], subcategory["icon"], subcategory["name"], subcategory["description"])
        mycursor.execute(sql, val)
        db.commit()
        return jsonify({"data":"OK retorne esto no más jeje"})
    except Exception as e:
       print('Error al crear la cuenta', e)
       return jsonify({"data":"no OK"})


#--read all--
@subcategories.route('/subcategories', methods=['GET'])
def getsubcategories():
    try:
        print("obtener cuentas")
        mycursor.execute("SELECT * FROM subcategories")
        results = mycursor.fetchall()
        subcategories = []
        """    print(results) """
        for subcategory in results:
            subcategories.append({
                'id': subcategory[0],
                'category_id': subcategory[1],
                'color': subcategory[2],
                'icon': subcategory[3],
                'name': subcategory[4],
                'description': subcategory[5]
                })
            
        for x in subcategories:
            print(x)
        
        return jsonify(subcategories)
    except Exception as e:
       print('Error al obtener las cuentas', e)


#--Leer subcategorias + categorias

@subcategories.route('/subcategories-detail', methods=['GET'])
def getsubcategories():
    try:
        print("Obteniendo detalles de subcategorias")
        mycursor.execute("SELECT * FROM subcategories_detail")
        results = mycursor.fetchall()
        subcategories = []
        """    print(results) """
        for subcategory in results:
            subcategories.append({
                'id': subcategory[0],
                'name': subcategory[1],
                'category': subcategory[2],
                'color': subcategory[3],
                'icon': subcategory[4],
                })
            
        for x in subcategories:
            print(x)
        
        return jsonify(subcategories)
    except Exception as e:
       print('Error al obtener las cuentas', e)

#--read--------------------------------------------------->
@subcategories.route('/subcategories/<id>', methods=['GET'])
def getcategory(id):
    print("obteniendo cuenta unica", id)
    try:
        sql = ("SELECT * FROM subcategories WHERE id = %s")
        filtro = (id,)
        print(filtro, id)
        mycursor.execute(sql, filtro)
        result = mycursor.fetchall()
        print(result)
        return jsonify({"cuenta":result})
    except Exception as e:
       print('Error al obtener la cuenta', e)
       return jsonify({e: "error"})

  


#--update-------------------------------------------------->
@subcategories.route('/subcategories/<id>', methods=['PUT'])
def updateClient(id):
    try:
        print("editando cliente", id)
        print(request.json)
        subcategory = request.json
        sql = "UPDATE subcategories SET category_id = %s, color = %s, icon = %s, name = %s, description = %s where id = %s"
        val = (subcategory["category_id"],subcategory["color"], subcategory["icon"], subcategory["name"], subcategory["description"], id)
        mycursor.execute(sql, val)
        db.commit()
        return jsonify({"data":"*Si se logró agregar cliente"})
    except Exception as e:
       print('error al actualizar el cliente', e)
       return jsonify({"data":"*No se logró agregar cliente"})

#--delete
@subcategories.route('/subcategories/<id>', methods=['DELETE'])
def deleteUser(id):
    try:
        sql = "DELETE FROM subcategories WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        db.commit()
        return jsonify({'message': 'Dispositivo eliminado'})
    except Exception as e:
       print('error al actualizar el cliente', e)
       return jsonify({"data":"*No se logró eliminar la cuenta"})
