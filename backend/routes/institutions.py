from flask import Flask, jsonify, request, Blueprint
from db.db import mycursor
from db.db import db

print("Iniciando instituciones")

institutions = Blueprint('institutions', __name__)


#---------Cuentas personales------------

#--create--
@institutions.route('/institutions', methods=['POST'])
def createAccount():
    print("Crear institucion")
    try:
        print("Creando institucion")
        institution = request.json
        print(institution)
        sql = "INSERT INTO institutions (name, avatar, color, country) values (%s, %s, %s, %s)"
        val = (institution["name"], institution["avatar"], institution["color"], institution["country"],)
        mycursor.execute(sql, val)
        db.commit()

        sql = ("SELECT * FROM institutions ORDER BY id DESC limit 1")
        mycursor.execute(sql)
        result = mycursor.fetchall()
        institution = result[0]
        print(result)
        institution = {
                'id': institution[0],
                'name': institution[1],
                'avatar': institution[2],
                'color': institution[3],
                }

        return jsonify({"msg":"Institución creada correctamente creada correctamente"},{'Institucion':institution})
    except Exception as e:
       print('Error al crear la institucion', e)
       return jsonify({"msg":"No se logró crear Institucion"})


#--read all--
@institutions.route('/institutions', methods=['GET'])
def getAccounts():
    try:
        print("obtener Institucions")
        mycursor.execute("SELECT * FROM institutions")
        results = mycursor.fetchall()
        institutions = []
        print(results)
        for institution in results:
            institutions.append({
                'id': institution[0],
                'name': institution[1],
                'avatar': institution[2],
                'color': institution[3],
                })
            
        for x in institutions:
            print(x)
        
        return jsonify(institutions)
    except Exception as e:
       print('Error al obtener las Institucions', e)

#--read--------------------------------------------------->
@institutions.route('/institutions/<id>', methods=['GET'])
def getAccount(id):
    print("Obteniendo Institucion unica", id)
    try:
        sql = ("SELECT * FROM institutions WHERE id = %s")
        filtro = (id,)
        print(filtro, id)
        mycursor.execute(sql, filtro)
        result = mycursor.fetchall()
        institution = result[0]
        print(result)
        institution = {
                'id': institution[0],
                'name': institution[1],
                'avatar': institution[2],
                'color': institution[3],
                }
        return jsonify({"msg":"Cuenta obtenida correctamente"},{"Institucion":institution})
    except Exception as e:
       print('Error al obtener la Institucion', e)
       return jsonify({e: "error"})

  


#--update-------------------------------------------------->
@institutions.route('/institutions/<id>', methods=['PUT'])
def updateClient(id):
    try:
        print("editando cliente", id)
        print(request.json)
        institution = request.json
        sql = "UPDATE institutions set name = %s, avatar = %s, color = %s, country = %s WHERE id = %s"

        val = (institution["name"], institution["avatar"], institution["color"], institution["country"], id)
        mycursor.execute(sql, val)
        db.commit()

        sql = "SELECT * FROM institutions where id = %s"
        filtro = (id,)
        mycursor.execute(sql, filtro)
        result = mycursor.fetchall()
        institution = result[0]
        print(result)
        
        institution = {
                'id': institution[0],
                'name': institution[1],
                'avatar': institution[2],
                'color': institution[3],
                }

        return jsonify({"msg":"Cliente editado correctamente"},{"Institución":institution})
    except Exception as e:
       print('error al actualizar el cliente', e)
       return jsonify({"msg":"*No se logró editar la institución"})

#--delete
@institutions.route('/institutions/<id>', methods=['DELETE'])
def deleteUser(id):
    try:
        sql = "DELETE FROM institutions WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        db.commit()
        return jsonify({'msg': 'Cuenta eliminada correctamente'}, {"id":id})
    except Exception as e:
       print('No se logró eliminar la institución', e)
       return jsonify({"msg":"*No se logró eliminar la Institución"})
