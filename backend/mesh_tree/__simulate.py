from mesh_tree.__clients import clients
from mesh_tree.__show_mesh import show_mesh
""" from __clients import clients
from __show_mesh import show_mesh """
import time

def delay(sec):
    time.sleep(sec)
    print("El delay ha terminado")

def get_data_from_wlc():
    try:
        
        print("Simulando conección a WLC")
        delay(1)
        print("Conexión existosa")
        delay(1)

        clients_summary = clients
        mesh_tree = show_mesh
        data = {
            "clients": clients_summary,
            "aps": mesh_tree
            }
        print("Se obtuvo la data desde WLC")
        #print(data)
        return data
    
    except Exception as e:
        print("No se logró simular data desde WLC",e)
        return "*No se logró recuperar data desde WLC"


    
