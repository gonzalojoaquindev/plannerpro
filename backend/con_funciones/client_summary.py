#from data_pruebas.clients import clients
from mesh_ap import formater_aps

def formater_clients(text_client):
    #clientes = clients.replace('\n', '*').split('*')
    clientes = text_client.replace('\n', '*').split('*')
    cliente1 = []
    clientList = []

    #Lo separo en elementos
    for variable in clientes:
        if "Disassociated" in variable:
            modificada = variable.replace("Disassociated", "Disassociated ").split()
            cliente1.append(modificada)
        else:
            cliente = variable.split()
            cliente1.append(cliente)

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
    return clientList


