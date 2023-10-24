import numpy as np

def test():
    x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

    primero = x[0]
    ultimo = x[-1]
    segundo = x[1]
    penultimo = x[-2]

    print(f'priemero = {primero}. segundo = {segundo} .... penultimo = {penultimo} ultimo={ultimo}')
    print(type(penultimo))

    rango = x[2:5]
    print(f'rango(2 a 5): {rango}')
    print(type(rango))


if __name__ == "__main__":
    test()