from flask import Flask, jsonify, request, Blueprint
#from netmiko import ConnectHandler
from netmiko import (ConnectHandler, NetmikoTimeoutException)
from client_detail.formater_client_detail import formater_client
from pprint import pprint

client_detail = Blueprint('client_detail', __name__)


""" device = ConnectHandler(
    'device_type': 'cisco_wlc',
    'host':   '10.16.43.97',
    'username': 'garaya',
    'password': 'vE/vR3:299dj06',
    'port' : 22,          # optional, defaults to 22
    'secret': 'secret',
    'banner_timeout': 25     # optional, defaults to ''
) """

device = ConnectHandler(
    device_type= 'cisco_wlc',
    host=  '10.16.43.97',
    username= 'garaya',
    password= 'vE/vR3:299dj06',
    port= 22,          # optional, defaults to 22
    secret= 'secret',
    banner_timeout= 25     # optional, defaults to ''
)

#intentar iterar los comandos  y mandarselos con el array



lista = [
    {
    "hostname": "Pala S01 FMS",
    "MAC": "00:30:1a:4e:dd:45"
    },
    {
    "hostname": "Pala S02 FMS",
    "MAC": "00:30:1a:4e:9f:80"
    },
    {
    "hostname": "PALA S02 CAS",
    "MAC": "c4:93:00:32:63:85"
    },
    {
    "hostname": "PALA S02 CAS B",
    "MAC": "c4:93:00:2e:a4:53"
    },
    {
    "hostname": "Pala Sh02 FMS",
    "MAC": "00:30:1a:4e:dd:74"
    }
]


""" def open_connection_wlc():
    try:
        print("Conectando con WLC para obener detalles de clientes")
        net_connect = ConnectHandler(**wlc)
        if net_connect.is_alive():
            print("Conexión exitosa con WLC")
            return(True)
        else:
            print("No se logró conexión con WLC")
            return(False)
    except Exception as e:
        print("No se logró procesar la solicitud",e)

connection = open_connection_wlc()
print("connection", connection)
 """




@client_detail.route('/clients_detail', methods=['GET'])
def get_client_detail():
    try:
        print("Conectando con WLC para obener detalles de clientes")
        #net_connect = ConnectHandler(**wlc)
        if device.is_alive():
            print("Conexión exitosa con WLC")
            
        #print(data)
           
        else:
            print("No se logró conexión con WLC",)
            return jsonify({"data":"*No se logró conectar con WLC", "error": e})
            
        
    except Exception as e:
        exception_type = type(e).__name__
        if exception_type == 'NetmikoTimeoutException':
            print("me botaste")
            device.disconnect()
            print("Intentando reconectar")
            device.send_command("show version")

        print("el tipo de error es:", exception_type)
        print("No se logró procesar la solicitud",e)
        return jsonify({"data":"No se logró resolver solicitud"})
    
    else:
        print("se conectó perfectamente")
        try: 
            clientes = []
            for item in lista:
                #print(f"show client detail {item['MAC']}")
                result = device.send_command(f"show client detail {item['MAC']}")
                #result = net_connect.send_command("show client detail c4:93:00:2e:a4:53")
                data = {
                    "hostname": item["hostname"],
                    "data": result
                    }
                clientes.append(data)
                print(f"Se obtuvo la data de ${item['hostname']}")
        except Exception as e:
                print("No se logró recuperar los datos de los clientes del WLC",e)
                return jsonify({"data":"No se logró resolver solicitud"})
        else:
            res = formater_client(clientes)
            print(res[1]["rssi"], res[1]["snr"])
            return jsonify (res)
    finally:
        print("solicitud terminada")
    


