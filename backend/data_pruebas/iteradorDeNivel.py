from pprint import pprint
""" lista= [
    {"nivel":1, "nombre":"carro01"},
    {"nivel":2, "nombre":"carro02"},
    {"nivel":1, "nombre":"carro03"},
    {"nivel":3,"nombre":"carro04"},
    {"nivel":3,"nombre":"carro05"},
    {"nivel":2,"nombre":"carro06"},
    {"nivel":3,"nombre":"carro07"},
    {"nivel":1,"nombre":"carro08"},
    {"nivel":3,"nombre":"carro09"},
    {"nivel":1,"nombre":"carro10"},
    {"nivel":3,"nombre":"carro11"},
    {"nivel":2,"nombre":"carro12"},
]

for elemento in reversed(lista):
    print(elemento) """


def agregar_padre(lista_diccionarios):
  """
  Agrega el campo "padre" a los diccionarios de la lista, considerando el campo ascendente directo.

  Args:
    lista_diccionarios: La lista de diccionarios a los que se agregará el campo "padre".

  Returns:
    La lista de diccionarios con el campo "padre" agregado.
  """
lista = [
{"nivel":0,"nombre":"wlc"},
  {"nivel": 1, "nombre": "carro01"},
  {"nivel": 2, "nombre": "carro02"},
  {"nivel": 2, "nombre": "carro03"},
  {"nivel": 3, "nombre": "carro04"},
  {"nivel": 3, "nombre": "carro05"},
  {"nivel": 2, "nombre": "carro06"},
  {"nivel": 3, "nombre": "carro07"},
  {"nivel": 1, "nombre": "carro08"},
  {"nivel": 3, "nombre": "carro09"},
  {"nivel": 1, "nombre": "carro10"},
  {"nivel": 3, "nombre": "carro11"},
  {"nivel": 2, "nombre": "carro12"},
]
lista_diccionarios_con_padre = []

lista_sin_padres = lista.copy()
#print(lista_sin_padres)

for inverso in reversed(lista_sin_padres):
  for correcto in reversed(lista_sin_padres):
    #print(inverso, correcto )
    if inverso["level"] -1 == correcto["level"]:
        print("encontré a mi padre", inverso["name"], correcto["name"])
        lista_sin_padres.remove(inverso)
        #print(f"elimando {inverso}")
        break


text = "  |-CM01-MAP-01[1,28,ANTU,(157,161),None,21%,1]"

def format_subnode(string):
    formatted = string.lstrip().replace('|-','').replace("[",",").replace("]","").split(",")
    return formatted

print(format_subnode(text))

""" for item in reversed((lista_sin_padres)):
  print(item)
  lista_sin_padres.remove(item)
  print(f"se eliminó el elemento {item}") """

#lista_con_padre = agregar_padre(lista)


#pprint(lista_con_padre)



""" 
 for inverso in reversed(lista_diccionarios):
    diccionario_padre = None

    for diccionario_anterior in lista_diccionarios_con_padre:
      print(diccionario_anterior["nombre"],diccionario_anterior["nivel"], elemento["nivel"], elemento["nombre"])
      if diccionario_anterior["nivel"] > inverso["nivel"]:
        print("encontre el padre", diccionario_anterior, elemento)
        diccionario_padre = diccionario_anterior["nombre"]
        break

    inverso["padre"] = diccionario_padre

    lista_diccionarios_con_padre.append(elemento)

  return lista_diccionarios_con_padre
 """