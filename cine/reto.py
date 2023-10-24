import numpy as np
import json

def cargarDatos(archivo):
    with open(archivo, "r") as file:
        data = json.load(file)
    return data

def procesarProductos(data):
    datosProductos = []
    for item in data["ventas"]:
        cantidades = list(item["unidades"].values())
        datosProductos.append(cantidades)
    ventas = np.array(datosProductos)
    return ventas

if __name__ == '__main__':
    data = cargarDatos("ventas.json")
    datosXproducto = procesarProductos(data)

    promedio = np.mean(datosXproducto, axis=1)
    desv = np.std(datosXproducto, axis=1)

    for i, item in enumerate(data["ventas"]):
        print(f'Producto: {item["producto"]}')
        print(f'   Promedio: {round(promedio[i],2)}')
        print(f'   Desviación estandar: {round(desv[i],3)}')
        print('-----------------------------')
    