from flask import jsonify, request, Blueprint
from db.db import mycursor
from db.db import db
print("iniciando categorias")


categories = Blueprint('categories', __name__)


#---------Categrias------------

#--create--
@categories.route('/categories', methods=['POST'])
def createcategory():
    print("crear cuenta")
    try:
        print("estoy dentro del bloque try")
        category = request.json
        print(category)
        print(category["name"])
        sql = "INSERT INTO categories (color, icon, name, description) VALUES (%s, %s, %s, %s)"
        val = (category["color"], category["icon"], category["name"], category["description"])
        
        """ sql = "INSERT INTO categories (institution_id, name, color,type, credit_quote, credit_used, payment_date, start_billed_period, end_billed_period, billing_date, debit, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (category["institution_id"], category["name"], category["color"], category["type"], category["credit_quote"], category["credit_used"], category["payment_date"], category["start_billed_period"], category["end_billed_period"], category["billing_date"], category["debit"], category["user_id"]) """
        """ sql = "INSERT INTO categories (institution_id, user_id, name, color, type, debit, credit_limit, credit_used, payment_date, start_billed_period, end_billed_period) VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (category["institution_id"], category["user_id"], category["name"], category["color"], category["type"], category["debit"], category["credit_limit"], category["credit_used"], category["available_credit"], category["payment_date"], category["start_billed_period"], category["end_billed_period"], category["available_total"], category["balance"]) """
        mycursor.execute(sql, val)
        db.commit()
        return jsonify({"data":"OK retorne esto no más jeje"})
    except Exception as e:
       print('Error al crear la cuenta', e)
       return jsonify({"data":"no OK"})


#--read all--
@categories.route('/categories', methods=['GET'])
def getCategories():
    try:
        print("Obteniendo categorias")
        mycursor.execute("SELECT * FROM categories")
        results = mycursor.fetchall()
        categories = []
        """  print(results) """
        for category in results:
            categories.append({
                'id': category[0],
                'color': category[1],
                'icon': category[2],
                'name': category[3],
                'description': category[4]
                })
            
        """ for x in categories:
            print(x) """
        print(f"Se obtuvieron {len(categories)} categorias")
        
        return jsonify(categories)
    except Exception as e:
       print('Error al obtener las cuentas', e)
       return jsonify({"msg":"No se logró obtener las categorias"})

#--read--------------------------------------------------->
@categories.route('/categories/<id>', methods=['GET'])
def getcategory(id):
    print("obteniendo cuenta unica", id)
    try:
        sql = ("SELECT * FROM categories WHERE id = %s")
        filtro = (id,)
        print(filtro, id)
        mycursor.execute(sql, filtro)
        result = mycursor.fetchall()
        print(result)
        return jsonify({"cuenta":result})
    except Exception as e:
       print('Error al obtener las categorias', e)
       return jsonify({"msg":"No se logró obtener la categoria"})

  


#--update-------------------------------------------------->
@categories.route('/categories/<id>', methods=['PUT'])
def updateClient(id):
    try:
        print("editando cliente", id)
        print(request.json)
        category = request.json
        sql = "UPDATE categories SET color = %s, icon = %s, name = %s, description = %s where id = %s"
        val = (category["color"], category["icon"], category["name"], category["description"], id)
        mycursor.execute(sql, val)
        db.commit()
        return jsonify({"data":"*Si se logró agregar cliente"})
    except Exception as e:
       print('error al actualizar el cliente', e)
       return jsonify({"data":"*No se logró agregar cliente"})

#--delete
@categories.route('/categories/<id>', methods=['DELETE'])
def deleteUser(id):
    try:
        sql = "DELETE FROM categories WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        db.commit()
        return jsonify({'message': 'Dispositivo eliminado'})
    except Exception as e:
       print('error al actualizar el cliente', e)
       return jsonify({"data":"*No se logró eliminar la cuenta"})
