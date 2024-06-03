from pymongo import MongoClient
from backend.obsoletos.client_summary import clientList
mongoClient = MongoClient("localhost",27017)
db = mongoClient.monitorTree

collection = db.clients

try:
    collection.insert_many(clientList)
    print("Se han guardado exitosamente")
except Exception as e:
    print(e)






