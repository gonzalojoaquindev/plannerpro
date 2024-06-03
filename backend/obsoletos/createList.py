from pprint import pprint
from backend.obsoletos.mesh_ap import apList
from backend.obsoletos.client_summary import clientList


from pymongo import MongoClient
from backend.obsoletos.client_summary import clientList
mongoClient = MongoClient("localhost",27017)
db = mongoClient.monitorTree

#elimino la lista anterior
try:
    db.clientList.delete_many({})
    db.apList.delete_many({})
    print("Se han eliminados todos los datos anteriores de apList y clientList en MongoDB")  
except Exception as e:
    print(e)

#envio la nueva lista
try:
    db.clientList.insert_many(clientList)
    db.apList.insert_many(apList)
    print("Se han guardado las nuevas listas de ap y clientes exitosamente en mongoDB")  
except Exception as e:
    print(e)


#trigo la lista con el hostname
pipeline = [
    {'$lookup': {
        'from': "inventary",
        'localField': "ip",
        'foreignField': "inventary_ip",
        'as': "fromInventary"
        }
    },
    {
    '$replaceRoot': 
        { 
            'newRoot': 
            { '$mergeObjects': [{ '$arrayElemAt': ["$fromInventary", 0] }, "$$ROOT"] } 
        }
    },
    { '$project': { 'fromInventary': 0 } }
]


clients = list(db.clientList.aggregate(pipeline))


clientsListFinal = []
for client in clients:
    hostname = client.get("hostname")
    if hostname is None:
         clientsListFinal.append({
                "name": "cliente no registrado",
                "ip": client["ip"],
                "parent": client["ap"],
                "mac": client["mac"]
            })
       
        #print(f"El diccionario {ap} tiene el campo 'parent' vacío")
    else:
        #Aqui se fuerza a que se escriba el parent como el default_parent
       clientsListFinal.append({
                "name": client["hostname"],
                "ip": client["ip"],
                "parent": client["ap"],
                "mac": client["mac"]
            })
print("Se creó la lista final de clientes con sus hostname")
""" pprint(clientsListFinal) """


# Traigo los datos de los ap para saber si tiene un parent_default
pipelineAPS = [
    {'$lookup': {
        'from': "inventary",
        'localField': "name",
        'foreignField': "hostname",
        'as': "fromInventary"
        }
    },
    {
    '$replaceRoot': 
        { 
            'newRoot': 
            { '$mergeObjects': [{ '$arrayElemAt': ["$fromInventary", 0] }, "$$ROOT"] } 
        }
    },
    { '$project': { 'fromInventary': 0 } }
]

aps = list(db.apList.aggregate(pipelineAPS))

""" pprint(aps) """



#Función que permita establecer el parent por defecto
apListFinal = []
for ap in aps:
    parent = ap.get("parent_default")
    if parent is None or parent == "":
        if ap.get("inventary_ip"):
            apListFinal.append({
                "name": ap["name"],
                "ip": ap["inventary_ip"],
                "parent": ap["parent"],
                
            })
        else:
            apListFinal.append({
                "name": ap["name"],
                "ip": "IP no registrada",
                "parent": ap["parent"],
                
            })
        #print(f"El diccionario {ap} tiene el campo 'parent' vacío")
    else:
        #Aqui se fuerza a que se escriba el parent como el default_parent
        apListFinal.append({
            "name": ap["name"],
            "ip": ap["inventary_ip"],
            "parent": ap["parent_default"],
        })
        #print(f"El ap {ap} si tiene parent")
print("Se creó la lista final de APS con sus parent por defecto")

#Combino ambas listas
combined_list = clientsListFinal.copy()
combined_list.extend(apListFinal)

#pprint(combined_list)
print("Se creó la lista combinada de APs y clientes")
