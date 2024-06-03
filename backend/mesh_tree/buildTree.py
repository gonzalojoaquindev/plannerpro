from mesh_tree.createList import createList
from pprint import pprint

def get_rap(clients):
    rap = [client for client in clients if client["parent"] == "WLC"]
    return rap

def build_tree(clients):
    
    wlc = {"name": "WLC", "children": []}
    rap = get_rap(clients)
    for client in rap:
        wlc["children"].append({"name": client["name"], "children": [], "data": client["data"]})

    def add_children(node):
        children = [client for client in clients if client["parent"] == node["name"]]
        for client in children:
            node["children"].append({"name": client["name"], "children": [], "data": client["data"]})
        for child_node in node["children"]:
            add_children(child_node)

    for child_node in wlc["children"]:
        add_children(child_node)

    return wlc


#clientsActive = [client for client in data if client["parent"] != ""]



