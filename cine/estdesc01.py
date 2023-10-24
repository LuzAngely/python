


def promedio(datos):
    print("promedio(datos, datos1)")
    suma = 0
    for i in range(len(datos)):
        suma = suma + datos[i]
    promedio = suma / len(datos)
    return promedio

def max(datos):
    max = datos[0]
    for i in range(1,len(datos)):
        if max < datos[i]:
            max = datos[i]
    return max

def min(datos):
    min = datos[0]
    for i in range(1,len(datos)):
        if min > datos[i]:
            min = datos[i]
    return min

if __name__=='__main__':
    datosVentas = [1200, 3500, 869, 1431, 249, 1145, 20]
    
    print (f'Promedio de ventas es: {promedio(datosVentas)}')
    print (f'Maximo de ventas es:   {max(datosVentas)}')
    print (f'minimo de ventas es:   {min(datosVentas)}')


    
