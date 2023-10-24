import numpy as np
import json

def cargarDatos(archivo):
    with open(archivo, "r") as file:
        data = json.load(file)
    return data

def numeroNacimientos(data):
    datosNacimientos = []
    for sexo, datos_sexo in data['nacimientos'].items():
        cantidadNacimientos = []
        for year, meses in datos_sexo.items():
            cantidadNacimientos.extend(meses.values())
        datosNacimientos.append(cantidadNacimientos)
    nacimientos = np.array(datosNacimientos)
    return nacimientos

if __name__ == '__main__':
    data = cargarDatos("nacimientos.json")
    datosXNacimientos = numeroNacimientos(data)

    promedio = np.mean(datosXNacimientos, axis=1)
    desv = np.std(datosXNacimientos, axis=1)

    sexos = data['sexos']
    for i, sexo in enumerate(sexos):
        print(f'Sexo: {sexo}')
        print(f'   Promedio: {round(promedio[i], 2)}')
        print(f'   Desviación estándar: {round(desv[i], 3)}')
        print('-----------------------------')
