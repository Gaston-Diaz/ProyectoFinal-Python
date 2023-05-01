import json

def agregar_venta(datos_nuevos):
    with open('files/datos.json','r') as archivo:
        lista_ventas = json.load(archivo)
    if not lista_ventas:
        id_nuevo = 1
    else:
        id_nuevo = int(max(lista_ventas, key=lambda x:x['id'])['id']) + 1
    datos_nuevos['id'] = id_nuevo
    lista_ventas.append(datos_nuevos)
    with open('files/datos.json','w') as archivo:
        json.dump(lista_ventas,archivo,indent=4)

def leer_archivo():
    with open('files/datos.json','r') as file:
        datos = json.load(file)
    datos_para_tabla = []
    for dato in datos:
        datos_para_tabla.append([dato["-CODIGO-"], dato["-CANTIDAD-"],dato["-PRECIO-"],dato["-CATEGORIAS-"], dato["-FECHA-"]])
    return datos_para_tabla