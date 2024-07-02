from flask import Flask, jsonify, request, Blueprint
from db.db import mycursor
from db.db import db

print("iniciando cuentas")

accounts = Blueprint('accounts', __name__)


#---------Cuentas personales------------

#--create--
@accounts.route('/accounts', methods=['POST'])
def createAccount():
    print("crear cuenta")
    try:
        print("Creando cuentas personales")
        account = request.json
        print(account)
        sql = "INSERT INTO personal_accounts (institution_id, user_id, name, color,type, debit, credit_limit, credit_used, payment_date, start_billed_period, end_billed_period ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (account["institution_id"], account["user_id"], account["name"], account["color"], account["type"], account["debit"],account["credit_limit"], account["credit_used"], account["payment_date"], account["start_billed_period"], account["end_billed_period"])
        mycursor.execute(sql, val)
        db.commit()

        sql = ("SELECT * FROM personal_accounts ORDER BY id DESC limit 1")
        mycursor.execute(sql)
        result = mycursor.fetchall()
        account = result[0]
        print(result)
        account = {
                'id': account[0],
                'institution_id': account[1],
                'user_id': account[2],
                'name': account[3],
                'color': account[4],
                'type': account[5],
                'debit': account[6],
                'credit_limit': account[7],
                'credit_used': account[8],
                'payment_date': account[9],
                'start_billed_period': account[10],
                'end_billed_period': account[11]
                }

        return jsonify({"msg":"Cuenta creada correctamente"},{'cuenta':account})
    except Exception as e:
       print('Error al crear la cuenta', e)
       return jsonify({"msg":"No se logró crear cuenta"})


#--read all--
@accounts.route('/accounts', methods=['GET'])
def getAccounts():
    try:
        print("Obteniendo cuentas")
        mycursor.execute("SELECT * FROM personal_accounts")
        results = mycursor.fetchall()
        accounts = []
        """ print(results) """
        for account in results:
            accounts.append({
                'id': account[0],
                'institution_id': account[1],
                'user_id': account[2],
                'name': account[3],
                'color': account[4],
                'type': account[5],
                'debit': account[6],
                'credit_limit': account[7],
                'credit_used': account[8],
                'payment_date': account[9],
                'start_billed_period': account[10],
                'end_billed_period': account[11]
                })
            
        """ for x in accounts:
            print(x) """
        
        print(f"se otuvieron {len(accounts)} cuentas")
        
        return jsonify(accounts)
    except Exception as e:
       print('Error al obtener las cuentas', e)

#--read--------------------------------------------------->
@accounts.route('/accounts/<id>', methods=['GET'])
def getAccount(id):
    print("Obteniendo cuenta unica", id)
    try:
        sql = ("SELECT * FROM personal_accounts WHERE id = %s")
        filtro = (id,)
        print(filtro, id)
        mycursor.execute(sql, filtro)
        result = mycursor.fetchall()
        account = result[0]
        print(result)
        account = {
                'id': account[0],
                'institution_id': account[1],
                'user_id': account[2],
                'name': account[3],
                'color': account[4],
                'type': account[5],
                'debit': account[6],
                'credit_limit': account[7],
                'credit_used': account[8],
                'payment_date': account[9],
                'start_billed_period': account[10],
                'end_billed_period': account[11]
                }
        return jsonify({"msg":"Cuenta obtenida correctamente"},{"cuenta":account})
    except Exception as e:
       print('Error al obtener la cuenta', e)
       return jsonify({e: "error"})

  


#--update-------------------------------------------------->
@accounts.route('/accounts/<id>', methods=['PUT'])
def updateClient(id):
    try:
        print("editando cliente", id)
        print(request.json)
        account = request.json
        sql = "UPDATE personal_accounts set institution_id = %s, user_id = %s, name = %s, color = %s, type = %s, debit = %s, credit_limit = %s, credit_used = %s, payment_date = %s, start_billed_period = %s, end_billed_period = %s WHERE id = %s"

        val = (account["institution_id"], account["user_id"], account["name"], account["color"], account["type"],account["debit"], account["credit_limit"], account["credit_used"],account["payment_date"], account["start_billed_period"], account["end_billed_period"], id)
        mycursor.execute(sql, val)
        db.commit()

        sql = "SELECT * FROM personal_accounts where id = %s"
        filtro = (id,)
        mycursor.execute(sql, filtro)
        result = mycursor.fetchall()
        account = result[0]
        """ print(result) """
        
        account = {
                'id': account[0],
                'institution_id': account[1],
                'user_id': account[2],
                'name': account[3],
                'color': account[4],
                'type': account[5],
                'debit': account[6],
                'credit_limit': account[7],
                'credit_used': account[8],
                'payment_date': account[9],
                'start_billed_period': account[10],
                'end_billed_period': account[11]
                }

        return jsonify({"msg":"Cliente editado correctamente"},{"cuenta":account})
    except Exception as e:
       print('error al actualizar el cliente', e)
       return jsonify({"msg":"*No se logró agregar cliente"})

#--delete
@accounts.route('/accounts/<id>', methods=['DELETE'])
def deleteUser(id):
    try:
        sql = "DELETE FROM personal_accounts WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        db.commit()
        return jsonify({'msg': 'Cuenta eliminada correctamente'}, {"id":id})
    except Exception as e:
       print('error al actualizar el cliente', e)
       return jsonify({"msg":"*No se logró eliminar la cuenta"})
