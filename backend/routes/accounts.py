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


""" sql = "INSERT INTO users (id, name, email, password, avatar, initials, birthday) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = (2, 'Natalia', 'nati@gmail.com','123','','NR','1993-04-26')
mycursor.execute(sql, val)
db.commit() """

accounts = Blueprint('accounts', __name__)


#---------Cuentas personales------------

#--create--
@accounts.route('/accounts', methods=['POST'])
def createAccount():
    print("crear cuenta")
    try:
        print("estoy dentro del bloque try")
        account = request.json
        print(account)
        print(account["name"])
        sql = "insert into personal_accounts (name, debit) values (%s, %s)"
        val = (account["name"], account["debit"])
        
        """ sql = "INSERT INTO personal_accounts (institution_id, name, color,type, credit_quote, credit_used, payment_date, start_billed_period, end_billed_period, billing_date, debit, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (account["institution_id"], account["name"], account["color"], account["type"], account["credit_quote"], account["credit_used"], account["payment_date"], account["start_billed_period"], account["end_billed_period"], account["billing_date"], account["debit"], account["user_id"]) """
        """ sql = "INSERT INTO personal_accounts (institution_id, user_id, name, color, type, debit, credit_limit, credit_used, payment_date, start_billed_period, end_billed_period) VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (account["institution_id"], account["user_id"], account["name"], account["color"], account["type"], account["debit"], account["credit_limit"], account["credit_used"], account["available_credit"], account["payment_date"], account["start_billed_period"], account["end_billed_period"], account["available_total"], account["balance"]) """
        mycursor.execute(sql, val)
        db.commit()
        return jsonify({"data":"OK retorne esto no más jeje"})
    except Exception as e:
       print('Error al crear la cuenta', e)
       return jsonify({"data":"no OK"})


#--read all--
@accounts.route('/accounts', methods=['GET'])
def getAccounts():
    try:
        print("obtener cuentas")
        mycursor.execute("SELECT * FROM personal_accounts")
        results = mycursor.fetchall()
        accounts = []
        print(results)
        for account in results:
            accounts.append({
                'id': account[0],
                'name': account[3],
                'color': account[4],
                'type': account[5],
                'credit_used': account[8],
                'debit': account[6]
                })
            
        for x in accounts:
            print(x)
        

        """ for account in results:
            account.append({
                'id': account['id'],
                'name': account['name'],
                'color': account['color'],
                'type': account['type'],
                'credit_used': account['credit_used'],
                'debit': account['debit']
            })
        for x in accounts:
            print(x) """
        return jsonify(accounts)
    except Exception as e:
       print('Error al obtener las cuentas', e)

""" device = db.accounts.find_one({'_id': ObjectId(id)})
  print(device)
  return jsonify({
    '_id': str(ObjectId(device['_id'])),
    'inventory_ip': device['inventory_ip'],
    'hostname': device['hostname'],
    'parent_default': device['parent_default'],
    'service': device['service'],
    'tag': device['tag'],
    'equipment': device['equipment']
  }) """

#--read--------------------------------------------------->
@accounts.route('/accounts/<id>', methods=['GET'])
def getAccount(id):
    print("obteniendo cuenta unica", id)
    try:
        sql = ("SELECT * FROM personal_accounts WHERE id = %s")
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
@accounts.route('/accounts/<id>', methods=['PUT'])
def updateClient(id):
    try:
        print("editando cliente", id)
        print(request.json)
        account = request.json
        sql = "UPDATE personal_accounts SET name = %s, debit = %s where id = %s"
        val = (account["name"], account["debit"], id)
        mycursor.execute(sql, val)
        db.commit()

        #db.update_one({'_id': ObjectId(id)}, {"$set": request.json})

        return jsonify({"data":"*Si se logró agregar cliente"})
    except Exception as e:
       print('error al actualizar el cliente', e)
       return jsonify({"data":"*No se logró agregar cliente"})

#--delete
@accounts.route('/accounts/<id>', methods=['DELETE'])
def deleteUser(id):
    try:
        sql = "DELETE FROM personal_accounts WHERE id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        db.commit()
        return jsonify({'message': 'Dispositivo eliminado'})
    except Exception as e:
       print('error al actualizar el cliente', e)
       return jsonify({"data":"*No se logró eliminar la cuenta"})
