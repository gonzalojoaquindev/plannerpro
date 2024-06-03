from netmiko import ConnectHandler
import pprint
""" from backend.data_pruebas.clients import clients """

wlc = {
    'device_type': 'cisco_wlc',
    'host':   '10.16.43.97',
    'username': 'garaya',
    'password': 'vE/vR3:299dj06',
    'port' : 22,          # optional, defaults to 22
    'secret': 'secret',     # optional, defaults to ''
}


def get_data_from_wlc(lista):
    try:
        print("Conectando a WLC")
        net_connect = ConnectHandler(**wlc)
        print("Conexión existosa")
        clientes = []
        for item in lista:
            #print(f"show client detail {item['MAC']}")
            result = net_connect.send_command(f"show client detail {item['MAC']}")
            #result = net_connect.send_command("show client detail c4:93:00:2e:a4:53")
            print(result)
            data = {
            "hostname": item["hostname"],
            "data": result
            }
            clientes.append(data)
            print(f"Se obtuvo la data de ${item['hostname']}")
        #print(data)
        return clientes
    except Exception as e:
        """      print("No se logró recuperar data desde WLC",e) """
        return f"No se logró recuperar data desde WLC {e}"






   
