from netmiko import ConnectHandler
from backend.data_pruebas.clients import clients
print(clients)

wlc = {
    'device_type': 'cisco_wlc',
    'host':   '10.16.43.97',
    'username': 'garaya',
    'password': 'vE/vR3:299dj06',
    'port' : 22,          # optional, defaults to 22
    'secret': 'secret',     # optional, defaults to ''
}

def get_aps_from_wlc():
    try:
        print("Conectando a WLC")
        net_connect = ConnectHandler(**wlc)
        print("Conexión existosa")
        mesh_tree = net_connect.send_command('show mesh ap tree')
        print("Se obtuvieron los ap desde WLC")
        return mesh_tree
    except Exception as e:
        print(e)

def get_clients_from_wlc():
    try:
        print("Conectando a WLC")
        net_connect = ConnectHandler(**wlc)
        print("Conexión existosa")
        clients_summary = net_connect.send_command('show client summary ip')
        print("Se obtuvieron los clientes desde WLC")
        return clients_summary
    except Exception as e:
        print(e)
        
#mesh_tree = net_connect.send_command('show mesh ap tree')

""" 
try:
    print("Conectando a WLC")
    net_connect = ConnectHandler(**wlc)
    print("Conexión existosa")
except Exception as e:
    print(e)

mesh_tree = net_connect.send_command('show mesh ap tree')
clients_summary = net_connect.send_command('show client summary ip')


print("Se obtuvieron los datos desde WLC") """





   
