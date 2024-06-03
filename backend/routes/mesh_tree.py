from flask import Flask, jsonify, request, Blueprint
#from mesh_tree.__clients import clients
#from mesh_tree.__show_mesh import show_mesh

from mesh_tree.formater import formater_data 
from mesh_tree.createList import createList
from mesh_tree.buildTree import build_tree
import time

from netmiko import ConnectHandler
from pprint import pprint


wlc = {
    'device_type': 'cisco_wlc',
    'host':   '10.16.43.97',
    'username': 'garaya',
    'password': 'vE/vR3:299dj06',
    'port' : 22,          # optional, defaults to
    'secret': 'secret',     # optional, defaults to ''
}


def delay(sec):
    time.sleep(sec)

mesh_tree = Blueprint('mesh_tree', __name__)


@mesh_tree.route('/mesh_tree', methods=['GET'])
def get_data_from_wlc():
    try:
        """ print("Simulando conección a WLC")
        delay(1)
        print("Conexión existosa")
        delay(1) """

        print("Conectando a WLC")
        net_connect = ConnectHandler(**wlc)
        print("Conexión existosa")
        clients_summary = net_connect.send_command('show client summary ip')
        mesh_tree = net_connect.send_command('show mesh ap tree')

        """ clients_summary = clients
        mesh_tree = show_mesh """
        data = {
            "clients": clients_summary,
            "aps": mesh_tree
            }
    except Exception as e:
        print("No se logró obtener data desde WLC",e)
        return jsonify({"data":"*No se logró recuperar data desde WLC"})
    else:
        print("Se obtuvo la data correctamente desde WLC")
        try:
           formated = formater_data(data)
        except Exception as e:
            print("No se logró formatear",e)
            return jsonify({"data":"*No se logró formatear"})
        else:
            try:
                list = createList(formated)
                #print(list)
                
            except Exception as e:
                print("No se logró crear lista",e)
                return jsonify({"data":"*No se logró conexión con base de datos", "error": e})
            else:
                try: 
                    tree = build_tree(list)
                    return jsonify ({"data":tree, "status": "Se ha actualizado el árbol mesh exitosamente"})
                except Exception as e:
                    return jsonify({"data":"*No se logró construir el árbol mesh", "error": e})
        
    finally:
        print("solicitud terminada")
    
