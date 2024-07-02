from flask import Flask, jsonify, request, Blueprint
from db.db import mycursor
from db.db import db
import datetime
from dateutil.relativedelta import relativedelta, MO



print("iniciando transacciones planificadas")


""" sql = "INSERT INTO users (id, name, email, password, avatar, initials, birthday) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = (2, 'Natalia', 'nati@gmail.com','123','','NR','1993-04-26')
mycursor.execute(sql, val)
db.commit() """

planned_transactions = Blueprint('planned_transactions', __name__)


#---------Cuentas personales------------

#--create--
@planned_transactions.route('/planned_transactions', methods=['POST'])
def createTran():
    print("Agregar transacción planificada")
    try:
        print("Intentando crear")
        tran = request.json
        print(tran)
        sql = "INSERT INTO planned_transactions (category_id,user_id,benefited_id, account_id, expense, income, comment,type, firts_payment, deadline, replay, every, intervalo, ends, total_amount, pac) VALUES (%s, %s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s, %s, %s, %s)"
           
        val = tran["category_id"], tran["user_id"], tran["benefited_id"], tran["account_id"], tran["expense"], tran["income"], tran["comment"], tran["type"], tran["firts_payment"], tran["deadline"], tran["replay"], tran["every"], tran["intervalo"], tran["ends"], tran["total_amount"], tran["pac"]
        """ print("val", val)  """

        mycursor.execute(sql, val)
        db.commit()

        mycursor.execute("SELECT * FROM planned_transactions ORDER BY id DESC limit 1")
        result = mycursor.fetchall()
        item = result[0]
        """ print(item) """
        transaction = {
            'id': item[0],
            'category_id': item[1],
            'user_id': item[2],
            'benefited_id': item[3],
            'account_id': item[4],
            'expense': item[5],
            'income': item[6],
            'comment': item[7],
            'type': item[8],
            'firts_payment': item[9],
            'deadline': item[10],
            'replay': item[11],
            'every': item[12],
            'intervalo': item[13],
            'ends': item[14],
            'total_amount': item[15],
            'pac': item[16]
        }
        print("transaccion leida desde db", transaction)
        

        """ >>> datetime.timedelta(weeks=1)
        datetime.timedelta(7)
        >>> datetime.timedelta(days=7)
        datetime.timedelta(7) """
        
        "Función para crear las transacciones programadas ----"
        if transaction["replay"] == 1:
            print("Creando transacción programada")
            i = 1
            date = transaction["firts_payment"]
            every = transaction["every"]
            interval = transaction["intervalo"]
            end = transaction["ends"] - 1
            """ print("2024-02-25" + datetime.timedelta(weeks=1))
            print(datetime.timedelta(7))
            print(datetime.timedelta(days=7))
            print( datetime.timedelta(7)) """
            mes = "months"
            print(date + relativedelta(months = every))
            print(f"he seleccionado un {mes}")
            print(relativedelta(months = every))
            
            intervalo = {
                "year": relativedelta(years = every),
                "month": relativedelta(months = every),
                "week": relativedelta(weeks = every),
                "day": relativedelta(days = every)
                }
            print(date + intervalo[interval])
            """ print(date + datetime.timedelta(week=1)) """
            sql2 = "INSERT INTO scheduled_transactions (planned_id,repetition , date, comment) VALUES (%s, %s, %s,%s)"
            val2 =  (transaction["id"], i, date, "Primera inserción ")
            mycursor.execute(sql2, val2)
            db.commit()
            while i <= end:
                date = date + intervalo[interval]
                sql2 = "INSERT INTO scheduled_transactions (planned_id,repetition , date, comment) VALUES (%s, %s, %s,%s)"
                val2 =  (transaction["id"], i+1, date, "Insertados desde el bucle while")
                mycursor.execute(sql2, val2)
                db.commit()
                print(i)
                i += 1
            print("Programa terminado")


        return jsonify({"msg":"Transacción panificada ingresada con exito"},transaction)
    except Exception as e:
       print('Error al crear la transacción', e)
       return jsonify({"data":"no OK"})


#--read all--
@planned_transactions.route('/planned_transactions', methods=['GET'])
def getTransactions():
    try:
        print("Obtener transacciones")
        mycursor.execute("SELECT * FROM planned_transactions")
        results = mycursor.fetchall()
        planned_transactions = []
        print(results)
        for item in results:
            planned_transactions.append({
            'id': item[0],
            'category_id': item[1],
            'user_id': item[2],
            'benefited_id': item[3],
            'account_id': item[4],
            'expense': item[5],
            'income': item[6],
            'comment': item[7],
            'type': item[8],
            'firts_payment': item[9],
            'deadline': item[10],
            'replay': item[11],
            'every': item[12],
            'intervalo': item[13],
            'ends': item[14],
            'total_amount': item[15],
            'pac': item[16]
            })
            
        """ for x in planned_transactions:
            print(x) """

        return jsonify(planned_transactions)
    except Exception as e:
       print('Error al obtener las cuentas', e)


#--read--------------------------------------------------->
@planned_transactions.route('/planned_transactions/<id>', methods=['GET'])
def getTransaction(id):
    print("obteniendo transacción", id)
    try:
        sql = ("SELECT * FROM planned_transactions WHERE id = %s")
        filtro = (id,)
        print(filtro, id)
        mycursor.execute(sql, filtro)
        result = mycursor.fetchall()
        item = result[0]
        print(item)
        transaction = {
            'id': item[0],
            'category_id': item[1],
            'user_id': item[2],
            'benefited_id': item[3],
            'account_id': item[4],
            'expense': item[5],
            'income': item[6],
            'comment': item[7],
            'type': item[8],
            'firts_payment': item[9],
            'deadline': item[10],
            'replay': item[11],
            'every': item[12],
            'intervalo': item[13],
            'ends': item[14],
            'total_amount': item[15],
            'pac': item[16]
        }
        return jsonify(transaction)
    except Exception as e:
       print('Error al obtener la transaction', e)
       return jsonify({e: "error"})

  


#--update-------------------------------------------------->
@planned_transactions.route('/planned_transactions/<id>', methods=['PUT'])
def updateTran(id):
    try:
        print("editando cliente", id)
        print(request.json)
        tran = request.json
        sql = "UPDATE planned_transactions SET category_id = %s,user_id = %s,benefited_id = %s, account_id = %s, expense = %s, income = %s, comment = %s,type = %s, firts_payment = %s, deadline = %s, replay = %s, every = %s, intervalo = %s, ends = %s, total_amount = %s, pac = %s WHERE id = %s"

        val = (tran["category_id"], tran["user_id"], tran["benefited_id"], tran["account_id"], tran["expense"], tran["income"], tran["comment"], tran["type"], tran["firts_payment"], tran["deadline"], tran["replay"], tran["every"], tran["intervalo"], tran["ends"], tran["total_amount"], tran["pac"], id)
        mycursor.execute(sql, val)
        db.commit()

        sql = "SELECT * FROM planned_transactions where id = %s"
        filtro = (id,)
        mycursor.execute(sql, filtro)
        result = mycursor.fetchall()
        item = result[0]
        print(result)
        tran = {
            'id': item[0],
            'category_id': item[1],
            'user_id': item[2],
            'benefited_id': item[3],
            'account_id': item[4],
            'expense': item[5],
            'income': item[6],
            'comment': item[7],
            'type': item[8],
            'firts_payment': item[9],
            'deadline': item[10],
            'replay': item[11],
            'every': item[12],
            'interval*': item[13],
            'ends': item[14],
            'total_amount': item[15],
            'pac': item[16]
        }

           
        return jsonify({"msg":"Se editó el cliente correctamente"},{"planned_transaction": tran})
    except Exception as e:
       print('error al actualizar el cliente', e)
       return jsonify({"msg":"*No se logró agregar cliente"})

#--delete
@planned_transactions.route('/planned_transactions/<id>', methods=['DELETE'])
def deleteTran(id):
    try:
        sql = "DELETE FROM planned_transactions WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        db.commit()
        return jsonify({'msg': 'Transacción planificada eliminada con éxito'})
    except Exception as e:
       print('No se logró eliminar la transacción planificada', e)
       return jsonify({"data":"*No se logró eliminar la transacción planificada"})
