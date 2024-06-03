from backend.obsoletos.mesh_ap import apList
from backend.obsoletos.client_summary import clientList
from data_pruebas.json import data


WLC = {
    "name":"WLC",
    "children": []
}

#voy a dejar pendiente esta parte para dejar hacer pruebas con la data preparada
""" print("LISTA DE AP")
for ap in apList:
    print(ap)


print("LISTA DE CLIENTES")
for client in clientList:
    print(client) """

#voy a hacer una prueba con esta esta data que tenia preparara en la extension.
""" print("LISTA DE data")
for datas in data:
    print(datas) """


#---Inserto los raps es decir, los que tiene como padre al WLC---
def getRap(nodo):
    if (nodo['AP'] == "WLC"):
        return True

RAP = list(filter(getRap,data))

for nodo in RAP:
    WLC["children"].append({
        "name": nodo["hostname"],
        "children": []
        })







#---Itero sobre el resto de los elementos para formar el árbol según sus padres

for nodo in WLC["children"]:
    def getChildren(n):
        if (n['AP'] == nodo['name']):
            return True
    children = list(filter(getChildren, data))
    for n in children:
        #print("primer n", n, "nodo padre", nodo)
        nodo["children"].append({"name": n["hostname"],"children": []})

        def getGrandson(n2):
            if (n2['AP'] == nodo['name']):
                return True
        grandson = list(filter(getGrandson, data))
        for n2 in grandson:
            print("nieto", grandson, "padre", n2)
            """nodo["children"].append({"name": n2["hostname"],"children": []}) """
            """ def getChildren(n):
                if (n['AP'] == nodo['name']):
                    return True
            children = list(filter(getChildren,data))
            for n in children:
                nodo["children"].append({"name": n["hostname"],"children": []}) """
    
    
    #print(children)

""" for nodo in WLC["children"]:
    print(nodo) """


""" 
Esto está entre comillas por que es el ejemplo de javascript
const WLC = {
    name: "WLC",
    children: []
}

const getRap = () => {
    const RAP = clients.filter(n => n.AP === "WLC")
    RAP.map(n => WLC.children.push({ name: n.hostname, children: [] }))
}
getRap()

WLC.children.forEach(nodo => {
    Object.value
    const children = clientsActive.filter(n => n.AP === nodo.name)
    children.map(n => {
        nodo.children.push({ name: n.hostname, children: [] })

    })
    nodo.children.forEach(nodo => {
        const children2 = clientsActive.filter(n => n.AP === nodo.name)
        children2.map(n => {
            nodo.children.push({ name: n.hostname, children: [] })
        })
        nodo.children.forEach(nodo => {
            const children3 = clientsActive.filter(n => n.AP === nodo.name)
            children3.map(n => {
                nodo.children.push({ name: n.hostname, children: [] })
            })
        })


    })
})

 """