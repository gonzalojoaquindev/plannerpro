#from conectionWLC import get_data_from_wlc
from mesh_tree.__simulate import get_data_from_wlc
#from __simulate import get_data_from_wlc
import pprint




#def formater_data(data):
def formater_data(data):
    #data = get_data_from_wlc()
    print("Formateando")
    aps = data["aps"]
    clients = data["clients"]
    apList = formater_aps(aps)
    clientList = formater_clients(clients)
    print("Formateo finalizado")
    #print(apList)
    return {"clientList": clientList,"apList": apList}

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
            'type': 'client'
        }
        clientList.append(nombre)
    print("se creó la lista de clientes")
    return clientList

def formater_aps(text_ap):
    mesh_tree = text_ap
    array = mesh_tree.split('\n')
    # Quito en el encabezado que no sirve
    del array[0:5]

    # Borro los elementos vacios de la lista
    arraySinVacios = list(filter(bool, array))

    

    def format_subnode(string):
        formatted = string.lstrip().replace('|-','').replace("[",",").replace("]","").split(",")
        return formatted

   

    listWithLevels = []
    for variable in arraySinVacios:
        level = int((len(variable)-len(variable.lstrip()))/2) + 1
        item = variable + "," + str(level)
        listWithLevels.append(item)
        
    
    #limpio los que no necesito
    listSeparada = []
    for variable in listWithLevels:
        if variable.startswith("[Sector") or variable.startswith("---") or variable.startswith("Number"):
            continue
        else:
            listSeparada.append(format_subnode(variable))
    

    listWithChannels = [{"name":"WLC", "level":0}]
    #En ocaciones los tienen dos canales por lo que se desplazn los otros datos, asi que esta itración corrije eso
    for ap in listSeparada:
        if len(ap) == 10:
            channel = ap[4] + "-" + ap[5]
            pref_parent =  ap[6]
            channel_util = ap[7]
            clients= ap[8]
            level = int(ap[9])
        else:
            channel = ap[4]
            pref_parent=  ap[5]
            channel_util = ap[6]
            clients= ap[7]
            level = int(ap[8])
        listWithChannels.append({
                "name": ap[0],
                "hop": int(ap[1]),
                "snr": int(ap[2]),
                "channel": channel,
                "pref_parent": pref_parent,
                "channel_util": channel_util,
                "clients": clients,
                "level": level,
                "type": "Access Point"
                })
    print("lista separada")

    apList = [] 
    #Iteración para encontrar el nombre del padre
    for inverso in reversed(listWithChannels):
        for correcto in reversed(listWithChannels):
            #print(inverso, correcto )
            if inverso["level"] -1 == correcto["level"]:
                inverso["parent"] = correcto["name"]
                apList.append(inverso)
                listWithChannels.remove(inverso)
                #print(f"elimando {inverso}")
                break
    print("Se creó la lista de APS")
    return  apList



