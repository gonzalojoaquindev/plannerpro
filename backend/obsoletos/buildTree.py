from data_pruebas.json import data
from pprint import pprint
from backend.obsoletos.createList import combined_list

def get_rap(clients):
    rap = [client for client in clients if client["parent"] == "WLC"]
    return rap

def build_tree(clients):
    wlc = {"name": "WLC", "children": []}
    rap = get_rap(clients)
    for client in rap:
        wlc["children"].append({"name": client["name"], "children": []})

    def add_children(node):
        children = [client for client in clients if client["parent"] == node["name"]]
        for client in children:
            node["children"].append({"name": client["name"], "children": []})
        for child_node in node["children"]:
            add_children(child_node)

    for child_node in wlc["children"]:
        add_children(child_node)

    return wlc


clientsActive = [client for client in data if client["parent"] != ""]
#tree = build_tree(combined_list)

#print(tree)
