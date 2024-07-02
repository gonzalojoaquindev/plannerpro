from flask import Flask, jsonify, request, Blueprint
from db.db import mycursor
from db.db import db

print("Iniciando usuarios")

users = Blueprint('users', __name__)


#---------Usuarios------------

#--Create--
@users.route('/users', methods=['POST'])
def createAccount():
    print("Crear usuario")
    try:
        print("Creando usuario")
        user = request.json
        print(user)
        sql = "INSERT INTO users (username, name, email, password, avatar, initials, birthday) values (%s, %s, %s, %s, %s, %s, %s)"
        val = (user["username"], user["name"], user["email"], user["password"],user["avatar"], user["initials"], user["birthday"])
        mycursor.execute(sql, val)
        db.commit()

        sql = ("SELECT * FROM users ORDER BY id DESC LIMIT 1")
        mycursor.execute(sql)
        result = mycursor.fetchall()
        user = result[0]
        print(result)
        user = {
                'id': user[0],
                'username': user[1],
                'name': user[2],
                'email': user[3],
                'password': user[4],
                'avatar': user[5],
                'initials': user[6],
                'birthday': user[7]
                }
            
        return jsonify({"msg":"Usuario creado correctamente"},{"body":user})
    except Exception as e:
       print('Error al crear la usuario', e)
       return jsonify({"msg":"No se logró crear usuario"})


#--read all--
@users.route('/users', methods=['GET'])
def getAccounts():
    try:
        print("Intentando obtener usuarios...")
        mycursor.execute("SELECT * FROM users")
        results = mycursor.fetchall()
        users = []
        print(results)
        for user in results:
            users.append({
                'id': user[0],
                'username': user[1],
                'name': user[2],
                'email': user[3],
                'password': user[4],
                'avatar': user[5],
                'initials': user[6],
                'birthday': user[7]
                })
            
        for x in users:
            print(x)
        
        return jsonify({"msg":"Usarios obtenidos correctamente"},{"body":users})
    except Exception as e:
       print('Error al obtener usuarios', e)
       return jsonify({"msg": "Nose logró obtener usuarios"})

#--read--------------------------------------------------->
@users.route('/users/<id>', methods=['GET'])
def getAccount(id):
    print("Obteniendo usuario...", id)
    try:
        sql = ("SELECT * FROM users WHERE id = %s")
        filtro = (id,)
        print(filtro, id)
        mycursor.execute(sql, filtro)
        result = mycursor.fetchall()
        user = result[0]
        print(result)
        user = {
                'id': user[0],
                'username': user[1],
                'name': user[2],
                'email': user[3],
                'password': user[4],
                'avatar': user[5],
                'initials': user[6],
                'birthday': user[7]
                }
        return jsonify({"msg":"Usuario obtenido correctamente"},{"body":user})
    except Exception as e:
       print('Error al obtener la Institucion', e)
       return jsonify({e: "error"})

  


#--update-------------------------------------------------->
@users.route('/users/<id>', methods=['PUT'])
def updateClient(id):
    try:
        print("editando cliente", id)
        print(request.json)
        user = request.json
        sql = "UPDATE users set username  = %s, name  = %s, email  = %s, password = %s, avatar = %s, initials = %s, birthday = %s WHERE id = %s"

        val = (user["username"], user["name"], user["email"], user["password"], user["avatar"], user["initials"], user["birthday"], id)
        mycursor.execute(sql, val)
        db.commit()

        sql = "SELECT * FROM users WHERE id = %s"
        filtro = (id,)
        mycursor.execute(sql, filtro)
        result = mycursor.fetchall()
        user = result[0]
        print(result)
        
        user = {
                'id': user[0],
                'username': user[1],
                'name': user[2],
                'email': user[3],
                'password': user[4],
                'avatar': user[5],
                'initials': user[6],
                'birthday': user[7]
                }

        return jsonify({"msg":"Usuario editado correctamente"},{"body": user})
    except Exception as e:
       print('error al actualizar el usuario', e)
       return jsonify({"msg":"*No se logró editar el usuario"})

#--delete
@users.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
    try:
        sql = "DELETE FROM users WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        db.commit()
        return jsonify({'msg': 'Usuario eliminado correctamente'}, {"body": id})
    except Exception as e:
       print('No se logró eliminar la institución', e)
       return jsonify({"msg":"*No se logró eliminar el usuario"})
