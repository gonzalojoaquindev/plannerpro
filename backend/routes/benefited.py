from flask import Flask, jsonify, request, Blueprint
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  database= "plannerPro",
  user="root",
  password="mysql"
)

mycursor = db.cursor()

print("conectandome a base de datos")

table={
    1: "id",
    2: "nane",
    3: "birthday",
    4: "relationship"
}




benefited = Blueprint('benefited', __name__)


#---------Cuentas personales------------

#--create--
@benefited.route('/benefited', methods=['POST'])
def createcategory():
    print("crear cuenta")
    try:
        print("estoy dentro del bloque try")
        category = request.json
        print(category)
        print(category["name"])
        sql = "INSERT INTO benefited (color, icon, name, description) VALUES (%s, %s, %s, %s)"
        val = (category["color"], category["icon"], category["name"], category["description"])
        
        """ sql = "INSERT INTO benefited (institution_id, name, color,type, credit_quote, credit_used, payment_date, start_billed_period, end_billed_period, billing_date, debit, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (category["institution_id"], category["name"], category["color"], category["type"], category["credit_quote"], category["credit_used"], category["payment_date"], category["start_billed_period"], category["end_billed_period"], category["billing_date"], category["debit"], category["user_id"]) """
        """ sql = "INSERT INTO benefited (institution_id, user_id, name, color, type, debit, credit_limit, credit_used, payment_date, start_billed_period, end_billed_period) VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (category["institution_id"], category["user_id"], category["name"], category["color"], category["type"], category["debit"], category["credit_limit"], category["credit_used"], category["available_credit"], category["payment_date"], category["start_billed_period"], category["end_billed_period"], category["available_total"], category["balance"]) """
        mycursor.execute(sql, val)
        db.commit()
        return jsonify({"data":"OK retorne esto no más jeje"})
    except Exception as e:
       print('Error al crear la cuenta', e)
       return jsonify({"data":"no OK"})


#--read all--
@benefited.route('/benefited', methods=['GET'])
def getbenefited():
    try:
        print("obtener cuentas")
        mycursor.execute("SELECT * FROM benefited")
        results = mycursor.fetchall()
        benefited = []
        """    print(results) """
        for category in results:
            benefited.append({
                'id': category[0],
                'color': category[1],
                'icon': category[2],
                'name': category[3],
                'description': category[4]
                })
            
        for x in benefited:
            print(x)
        
        return jsonify(benefited)
    except Exception as e:
       print('Error al obtener las cuentas', e)

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
        return jsonify({"cuenta":result})
    except Exception as e:
       print('Error al obtener la cuenta', e)
       return jsonify({e: "error"})

  


#--update-------------------------------------------------->
@benefited.route('/benefited/<id>', methods=['PUT'])
def updateClient(id):
    try:
        print("editando cliente", id)
        print(request.json)
        category = request.json
        sql = "UPDATE benefited SET color = %s, icon = %s, name = %s, description = %s where id = %s"
        val = (category["color"], category["icon"], category["name"], category["description"], id)
        mycursor.execute(sql, val)
        db.commit()
        return jsonify({"data":"*Si se logró agregar cliente"})
    except Exception as e:
       print('error al actualizar el cliente', e)
       return jsonify({"data":"*No se logró agregar cliente"})

#--delete
@benefited.route('/benefited/<id>', methods=['DELETE'])
def deleteUser(id):
    try:
        sql = "DELETE FROM benefited WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        db.commit()
        return jsonify({'message': 'Dispositivo eliminado'})
    except Exception as e:
       print('error al actualizar el cliente', e)
       return jsonify({"data":"*No se logró eliminar la cuenta"})
