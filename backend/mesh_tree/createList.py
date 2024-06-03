from pprint import pprint
from mesh_tree.formater import formater_data
""" from pymongo import MongoClient """
import pymongo

mongoClient = pymongo.MongoClient("localhost",27017)
db = mongoClient.monitorTree


def createList(data):   
    """ data = formater_data() """
    clientList = data["clientList"]
    apList = data["apList"]
    #elimino la lista anterior
    try:
        with pymongo.timeout(5):
            print("intentando ingresar a base de datos")
            db.clientList.delete_many({})
            db.apList.delete_many({})
            print("Se han eliminados todos los datos anteriores de apList y clientList en MongoDB")  
    except pymongo.errors.ServerSelectionTimeoutError as ex:
        print("$Error no hay ningún servidor Mongo DB disponible para una operación", ex)
        return "No se ha podido ingresar a base de datos, para eliminar registros"
    except pymongo.errors.ConnectionFailure as ex:
        print("$Error de conexión fallida",ex)
    except pymongo.errors.ExecutionTimeout as ex:
        print("$Error de tiempo de ejecución",ex)

    

    #envio la nueva lista
    try:
        db.clientList.insert_many(clientList)
        db.apList.insert_many(apList)
        print("Se han guardado las nuevas listas de ap y clientes exitosamente en mongoDB")  
    except Exception as e:
        print(e)
        return e


    #trigo la lista con el hostname
    pipeline = [
        {'$lookup': {
            'from': "clients_inventory",
            'localField': "ip",
            'foreignField': "inventory_ip",
            'as': "fromInventory"
            }
        },
        {
        '$replaceRoot': 
            { 
                'newRoot': 
                { '$mergeObjects': [{ '$arrayElemAt': ["$fromInventory", 0] }, "$$ROOT"] } 
            }
        },
        { '$project': { 'fromInventory': 0 } }
    ]


    clients = list(db.clientList.aggregate(pipeline))


    

    clientsListFinal = []
    for client in clients:
        hostname = client.get("hostname")
        client
        if hostname is None:
            clientsListFinal.append({
                    "name": "cliente no registrado",
                    "parent": client["ap"],
                    "data":{
                        "ip": client["ip"],
                        "mac": client["mac"],
                        "snr": 0,
                        "type": "client",
                    }
                    
                })
        
            #print(f"El diccionario {ap} tiene el campo 'parent' vacío")
        else:
            #Aqui se fuerza a que se escriba el parent como el default_parent
            clientsListFinal.append({
                        "name": client["hostname"],
                        "parent": client["ap"],
                        "data":{
                            "ip": client["ip"],
                            "mac": client["mac"],
                            "snr": 15,
                            "type":"client",
                            "tag": client["tag"],
                            "equipment": client["equipment"],
                            "service": client["service"]
                        }
                        
                    })
    print("Se creó la lista final de clientes con sus hostname")
    


    # Traigo los datos de los ap para saber si tiene un parent_default
    pipelineAPS = [
        {'$lookup': {
            'from': "aps_inventory",
            'localField': "name",
            'foreignField': "name",
            'as': "fromInventory"
            }
        },
        {
        '$replaceRoot': 
            { 
                'newRoot': 
                { '$mergeObjects': [{ '$arrayElemAt': ["$fromInventory", 0] }, "$$ROOT"] } 
            }
        },
        { '$project': { 'fromInvontary': 0 } }
    ]

    aps = list(db.apList.aggregate(pipelineAPS))

   



    #Función que permita establecer el parent por defecto
    apListFinal = []
    for ap in aps:
        parent = ap.get("parent_default")
        if parent is None or parent == "":
            if ap.get("inventory_ip"):
                apListFinal.append({
                    "name": ap["name"],
                    "parent": ap["parent"],
                    "data": {
                        "ip": ap["inventory_ip"],
                        "snr": ap["snr"],
                        
                        "type": "Access Point"
                    }
                    
                    
                })
            else:
                apListFinal.append({
                    "name": ap["name"],
                    "parent": ap["parent"],
                    "data":{
                        "ip": "IP no registrada",
                        "snr": ap["snr"],
                       
                        "type": "Access Point"
                    }
                    
                    
                })
            #print(f"El diccionario {ap} tiene el campo 'parent' vacío")
        else:
            #Aqui se fuerza a que se escriba el parent como el default_parent
            apListFinal.append({
                "name": ap["name"],
                "ip": ap["inventory_ip"],
                "data":{
                    "parent": ap["parent_default"],
                   
                    "snr": ap["snr"],
                    "type": "Access Point"
                }
                
            })
            #print(f"El ap {ap} si tiene parent")
    print("Se creó la lista final de APS con sus parent por defecto")

    #Combino ambas listas
    combined_list = clientsListFinal.copy()
    combined_list.extend(apListFinal)

    for client in combined_list:
        pprint(client)
    print("Se creó la lista combinada de APs y clientes")

    return combined_list

