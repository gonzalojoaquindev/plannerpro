#from client_detail import get_data_from_wlc
#from client_detail.result import results

import random
import pprint

palas = [
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

#results = get_data_from_wlc(palas)

#print(results)


def get_random_int(min, max):
    min = int(min)  # Asegura que min sea un entero
    max = int(max)  # Asegura que max sea un entero
    return random.randint(min, max)  # Genera el número aleatorio



def formater_client(results):
    clients_list = []
    #separar el string en 
    for variable in results:
        data_separada = variable['data'].replace('\n', '*').split('*')
        client = {}
        
        for item in data_separada:
            hostname = variable["hostname"]
            client["hostname"] = hostname
            data = item.lstrip()
            if data.startswith("Signal to Noise Ratio"):
                snr = int(data.split(". ")[1].replace(' dB',''))
                client["snr"] = snr
            elif data.startswith("Client MAC Address"):
                mac = data.split(". ")[1].strip()
                client["mac"] = mac
            elif data.startswith("Radio Signal Strength Indicator"):
                rssi = int(data.split(". ")[1].replace(' dBm',''))
                #client = get_random_int(-90,-20)
                client["rssi"] = rssi
            elif data.startswith("IP Address"):
                ip = data.split(". ")[1]
                client["ip"]=ip
            elif data.startswith("AP Name"):
                ap_name = data.split(". ")[-1]
                client["ap"] = ap_name
            elif data.startswith("Channel."):
                channel = data.split(". ")[-1]
                client["channel"] = channel
            elif data.startswith("Wireless LAN Network Name"):
                ssid = data.split(". ")[-1]
                client["ssid"] = ssid
            else:
                continue
        
        #agregamos al final de la lista los datos del cliente
            
        clients_list.append(client)
    return clients_list



