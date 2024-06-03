from backend.mesh_tree.conectionWLC import get_data_from_wlc

def formater_aps():
    mesh_tree = get_data_from_wlc()["aps"]
    clients = get_data_from_wlc()["clients"]
    array = mesh_tree.split('\n')
    # Quito en el encabezado que no sirve
    del array[0:5]

    # Borro los elementos vacios de la lista
    arraySinVacios = list(filter(bool, array))

    apList = []

    def format_subnode(string):
        formatted = string.lstrip().replace('|-','').replace("[",",").replace("]","").split(",")
        return formatted

    ap_list_with_levels = [{"name":"WLC", "level":0}]

    for variable in arraySinVacios:
        #Para lineas que no sirven
        if variable.startswith("[Sector") or variable.startswith("---") or variable.startswith("Number"):
            # print(arraySinVacios.index(variable),"no sirve", variable)
            continue
        #Cuando es un hijo, un nieto o un tataranieto de un ap
        elif variable.startswith(" "):
            #le quito espacios en blanco y el signo °|-
            #Lo separo en elementos de lista.
            if variable.startswith("  |-"):
                ap = format_subnode(variable)
                ap_list_with_levels.append({"name":ap[0], "level":2})
                #print("soy un hijo" ,ap)
            elif variable.startswith("    |-"):
                ap = format_subnode(variable)
                ap_list_with_levels.append({"name":ap[0], "level":3})
                #print("soy un nieto", ap)
            elif variable.startswith("      |-"):
                ap = format_subnode(variable)
                ap_list_with_levels.append({"name":ap[0], "level":4})
                #print("soy un tataranieto", ap)
            else:
                continue
        #Cuando es un padre, es decir un AP que se conecta directamente al WLC (RAP)
        else:
            ap = variable.replace("[",",").replace("]","").split(",")
            #print("soy un padre", ap)
            ap_list_with_levels.append({
                "name": ap[0],
                #"hop": variableSeparada[1],
                #"snr": variableSeparada[2],
                #"channel": variableSeparada[4],
                #"pref_parent": variableSeparada[5],
                #"chan_util": variableSeparada[6],
                #"clients": variableSeparada[7],
                "parent": "WLC",
                "level":1
            })

    for inverso in reversed(ap_list_with_levels):
        for correcto in reversed(ap_list_with_levels):
            #print(inverso, correcto )
            if inverso["level"] -1 == correcto["level"]:
                #print("encontré a mi padre", inverso["name"], "es", correcto["name"])
                apList.append({"name":inverso["name"], "parent": correcto["name"] })
                ap_list_with_levels.remove(inverso)
                #print(f"elimando {inverso}")
                break
    print("Se creó la lista de APS")

    return {
        "apsList": apList,
        "clients": clients
    }

