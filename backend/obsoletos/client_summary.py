#from data_pruebas.clients import clients
from backend.obsoletos.conectionWLC import clients_summary

#clientes = clients.replace('\n', '*').split('*')
clientes = clients_summary.replace('\n', '*').split('*')

cliente1 = []
clientList = []

"""  cliente = variable.split()
        cliente1.append(cliente) """

for variable in clientes:
    if "Disassociated" in variable:
        modificada = variable.replace("Disassociated", "Disassociated ").split()
        cliente1.append(modificada)
    else:
        cliente = variable.split()
        cliente1.append(cliente)


""" for variable in clientes:
    cliente = variable.split()
    print("DisassociatedUnknown" in variable)
    cliente1.append(cliente)
    print(len(cliente1))
 """
# Elimino el encabezado que no me sirve
del cliente1[0:7]
# Elimino la ultima linea que tampoco me sirve
cliente1.pop()

for variable in cliente1:
    nombre = {
        'ap': variable[1],
        'ip': variable[3],
        'mac': variable[0],
    }
    clientList.append(nombre)
print("se creó la lista de clientes")

""" for variable in clientList:
    print(variable)
 """
""" for variable in cliente2:
    MONGO_COLLECTION.insert(variable) """