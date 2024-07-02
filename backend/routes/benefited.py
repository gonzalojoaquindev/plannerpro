from flask import Flask, jsonify, request, Blueprint
from db.db import mycursor
from db.db import db

print("iniciando beneficiados")


benefited = Blueprint('benefited', __name__)


#---------Beneficiados------------

#--create--
@benefited.route('/benefited', methods=['POST'])
def createcategory():
    print("Agregar nuevo beneficiado")
    try:
        print("Intentando crear nuevo beneficiado")
        benefited = request.json
        print(benefited)
        sql = "INSERT INTO benefited (name, birthday, relationship) VALUES (%s, %s, %s)"
        val = (benefited["name"], benefited["birthday"], benefited["relationship"])
        
        mycursor.execute(sql, val)
        db.commit()

        mycursor.execute("SELECT * FROM benefited ORDER BY id DESC limit 1")
        result = mycursor.fetchall()
        item = result[0]
        print(item)
        benefited = {
            "id": item[0],
            "name": item[1],
            "birthday": item[2],
            "relationship": item[3]
        }

        return jsonify({"msg":"Beneficiado agregado con exito"}, benefited)
    except Exception as e:
       print('Error al crear la cuenta', e)
       return jsonify({"data":"no OK"})


#--read all--
@benefited.route('/benefited', methods=['GET'])
def getBenefited():
    try:
        print("Obteniendo beneficiados")
        mycursor.execute("SELECT * FROM benefited")
        results = mycursor.fetchall()
        benefited = []
        """    print(results) """
        for item in results:
            benefited.append({
                'id': item[0],
                'name': item[1],
                'birthday': item[2],
                'relationship': item[3]
                })
            
        """ for x in benefited:
            print(x) """
        print(f"Se obtuvieron {len(benefited)} beneficiados")
        
        return jsonify(benefited)
        
    except Exception as e:
       print('Error al obtener las cuentas', e)
       return jsonify({"hola":"fallé"})

#--read--------------------------------------------------->
@benefited.route('/benefited/<id>', methods=['GET'])
def getcategory(id):
    print("obteniendo cuenta unica", id)
    try:
        sql = ("SELECT * FROM benefited WHERE id = %s")
        filtro = (id,)
        print(filtro, id)
        mycursor.execute(sql, filtro)
        result = mycursor.fetchall()
        print(result)
        benefited = {
            'id': result[0][0],
            'name': result[0][1],
            'birthday': result[0][2],
            'relationship': result[0][3]
        }
        return jsonify({"msg":"Benefidiado obtenido correctamente"},benefited)
    except Exception as e:
       print('Error al obtener la cuenta', e)
       return jsonify({e: "error"})

  


#--update-------------------------------------------------->
@benefited.route('/benefited/<id>', methods=['PUT'])
def updateClient(id):
    try:
        print("editando cliente", id)
        print(request.json)
        benefited = request.json
        sql = "UPDATE benefited SET name = %s, birthday = %s, relationship = %s where id = %s"
        val = (benefited["name"], benefited["birthday"], benefited["relationship"], id)
        mycursor.execute(sql, val)
        db.commit()
        return jsonify({"data":"Beneficiado editado correctamente"},{"id":id})
    except Exception as e:
       print('error al actualizar el cliente', e)
       return jsonify({"data":"No se logró agregar cliente"})

#--delete
@benefited.route('/benefited/<id>', methods=['DELETE'])
def deleteUser(id):
    try:
        sql = "DELETE FROM benefited WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        db.commit()
        return jsonify({'msg': 'Beneficiado eliminidado correctamente'}, {'id':id})
    except Exception as e:
       print('error al actualizar el cliente', e)
       return jsonify({"data":"*No se logró eliminar la cuenta"})
