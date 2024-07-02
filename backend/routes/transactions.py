from flask import jsonify, request, Blueprint
from db.db import mycursor
from db.db import db

print("iniciando transacciones")


""" sql = "INSERT INTO users (id, name, email, password, avatar, initials, birthday) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = (2, 'Natalia', 'nati@gmail.com','123','','NR','1993-04-26')
mycursor.execute(sql, val)
db.commit() """

transactions = Blueprint('transactions', __name__)


#---------Cuentas personales------------

#--create--
@transactions.route('/transactions', methods=['POST'])
def createTran():
    print("Agregar transacción")
    try:
        print("estoy dentro del bloque try")
        tran = request.json
        print(tran)
        sql = "INSERT INTO transactions (origin_account_id,destination_account_id,category_id,user_id,benefited_id,sheduled_id,date,expense, income, comments,type, sheduled) VALUES (%s, %s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"
           
        val = tran["origin_account_id"], tran["destination_account_id"], tran["category_id"], tran["user_id"], tran["benefited_id"], tran["sheduled_id"], tran["date"], tran["expense"], tran["income"], tran["comments"], tran["type"], tran["sheduled"]
        print("val", val) 

        mycursor.execute(sql, val)
        db.commit()

        mycursor.execute("SELECT * FROM transactions ORDER BY id DESC limit 1")
        result = mycursor.fetchall()
        item = result[0]
        print(item)
        transaction = {
            'id': item[0],
            'origin_account_id': item[1],
            'destination_account_id': item[2],
            'category_id': item[3],
            'user_id': item[4],
            'benefited_id': item[5],
            'sheduled_id': item[6],
            'date': item[7],
            'expense': item[8],
            'income': item[9],
            'comments': item[10],
            'type': item[11],
            'sheduled': item[12],
        }
        return jsonify({"msg":"Transacción ingresada con exito"},transaction)
    except Exception as e:
       print('Error al crear la transacción', e)
       return jsonify({"data":"no OK"})


""" #--read all--
@transactions.route('/transactions', methods=['GET'])
def getTransactions():
    try:
        print("Obtener transacciones")
        mycursor.execute("SELECT * FROM transactions")
        results = mycursor.fetchall()
        transactions = []
        print(results)
        for item in results:
            transactions.append({
                'id': item[0],
                'origin_account_id': item[1],
                'destination_account_id': item[2],
                'category_id': item[3],
                'user_id': item[4],
                'benefited_id': item[5],
                'sheduled_id': item[6],
                'date': item[7],
                'expense': item[8],
                'income': item[9],
                'comments': item[10],
                'type': item[11],
                'sheduled': item[12],
                })
            

        return jsonify(transactions)
    except Exception as e:
       print('Error al obtener las cuentas', e) """
            

#--read all--desde vista
@transactions.route('/transactions', methods=['GET'])
def getTransactions():
    try:
        print("Obteneniendo transacciones")
        mycursor.execute("SELECT * FROM transactions_summary")
        results = mycursor.fetchall()
        transactions = []
        """ print(results) """
        for item in results:
            transactions.append({
                'id': item[0],
                'fecha': item[1],
                'cuenta_origen': item[2],
                'cuenta_destino': item[3],
                'categoria': item[4],
                'Gasto': item[5],
                'Ingreso': item[6],
                'Tipo': item[7],
                'Beneficiado': item[8],
                'Comentarios': item[9],
                })
            
        """ for x in transactions:
            print(x) """
        print(f"Se obtuvieron {len(transactions)} transacciones")

        return jsonify(transactions)
    except Exception as e:
       print('Error al obtener las transacciones', e)
       return jsonify({"msg":"No se logró obtener transacciones"})


#--read--------------------------------------------------->
@transactions.route('/transactions/<id>', methods=['GET'])
def getTransaction(id):
    print("obteniendo transacción", id)
    try:
        sql = ("SELECT * FROM transactions WHERE id = %s")
        filtro = (id,)
        print(filtro, id)
        mycursor.execute(sql, filtro)
        result = mycursor.fetchall()
        item = result[0]
        print(item)
        transaction = {
            'id': item[0],
            'origin_account_id': item[1],
            'destination_account_id': item[2],
            'category_id': item[3],
            'user_id': item[4],
            'benefited_id': item[5],
            'sheduled_id': item[6],
            'date': item[7],
            'expense': item[8],
            'income': item[9],
            'comments': item[10],
            'type': item[11],
            'sheduled': item[12],
        }
        return jsonify(transaction)
    except Exception as e:
       print('Error al obtener la transaction', e)
       return jsonify({e: "error"})

  


#--update-------------------------------------------------->
@transactions.route('/transactions/<id>', methods=['PUT'])
def updateTran(id):
    try:
        print("editando cliente", id)
        print(request.json)
        tran = request.json
        sql = "UPDATE transactions SET origin_account_id = %s, destination_account_id = %s, category_id = %s, user_id = %s, benefited_id = %s, sheduled_id = %s, date = %s, expense = %s, income = %s, comments =%s, type = %s, sheduled_id = %s where id = %s"
        val = (tran["origin_account_id"], tran["destination_account_id"], tran["category_id"], tran["user_id"], tran["benefited_id"], tran["sheduled_id"], tran["date"], tran["expense"], tran["income"], tran["comments"], tran["type"], tran["sheduled_id"], id)
        mycursor.execute(sql, val)
        db.commit()


        return jsonify({"msg":"Se editó el cliente correctamente"})
    except Exception as e:
       print('error al actualizar el cliente', e)
       return jsonify({"msg":"*No se logró agregar cliente"})

#--delete
@transactions.route('/transactions/<id>', methods=['DELETE'])
def deleteTran(id):
    try:
        sql = "DELETE FROM transactions WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        db.commit()
        return jsonify({'message': 'Dispositivo eliminado'})
    except Exception as e:
       print('error al actualizar el cliente', e)
       return jsonify({"data":"*No se logró eliminar la cuenta"})


#---Obtener todos las caracteristicas
@transactions.route('/transactions/all', methods=['GET'])
def getTranAll():
    try:
        mycursor.execute("SELECT * FROM benefited")
        results = mycursor.fetchall()
        transactions = []
        print(results)
        for item in results:
            transactions.append({
                'id': item[0],
                'origin_account_id': item[1],
                'destination_account_id': item[2],
                'category_id': item[3],
                'user_id': item[4],
                'benefited_id': item[5],
                'sheduled_id': item[6],
                'date': item[7],
                'expense': item[8],
                'income': item[9],
                'comments': item[10],
                'type': item[11],
                'sheduled': item[12],
                })

    except Exception as e:
       print('error al actualizar el cliente', e)
       return jsonify({"data":"*No se logró eliminar la cuenta"})
