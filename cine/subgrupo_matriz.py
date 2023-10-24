import numpy as np

def test_matriz():

    matriz = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
    #indexacion
    centro = matriz[1, 1]
    primera_fila = matriz[0, :]
    primera_columna = matriz[:, 0]
    ultima_colunma = matriz[:, -1]

    print(matriz)
    print(ultima_colunma)


    #slicing
    sub_matriz = matriz[1:3, 0:1]
    primeras2filas = matriz[:2, :]
    maxesp = np.max(matriz[:2, 1:])
    print('-------------')
    print(matriz[:2, 1:])
    print(maxesp)

if __name__ == '__main__':
    test_matriz()