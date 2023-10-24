import numpy as np   #ejecurtar comando pip install numpy

if __name__ == '__main__':
    datosVentas = np.array([1200, 3500, 869, 1431, 249, 1145, 20])

    print (f'Promedio de ventas es: {np.mean(datosVentas)}')
    print (f'Maximo de ventas es:   {np.max(datosVentas)}')
    print (f'Minimo de ventas es:   {np.min(datosVentas)}')

    #matrices
    matrixDatos1 = np.array([[1, 2], [3, 4]])
    matrixDatos2 = np.array([[5, 6], [7, 8]])

    suma = matrixDatos1 + matrixDatos2
    producto_punto = np.dot(matrixDatos1,matrixDatos2)
    producto_cruz = np.cross(matrixDatos1,matrixDatos2)
    #print(f' matrixDatos1 -> {type(matrixDatos1)}')
    #print(f' matrixDatos2 -> {type(matrixDatos2)}')

    #print(f' producto_punto -> {type(producto_punto)} {producto_punto}')

    print("MAtrix 1")
    for i in matrixDatos1:
        print(i)

    print("MAtrix 2")
    for i in matrixDatos2:
        print(i)

    print("MAtrix 1 + matrix2")
    for i in suma:
        print(i)

    print("MAtrix 1 ° matrix2")
    for i in producto_punto:
        print(i)
    
    print("MAtrix 1 x matrix2")
    for i in producto_cruz:
        print(i)
