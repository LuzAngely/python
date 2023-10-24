#espacio para librerias y paquetes

#espacio para funciones y clase
def compararPrecio(hamb1, hamb2):
    if hamb1 > hamb2:
        return True
    else:
        return False


def datos ():
    H1 = int(input("Cuanto cuesta H1? "))
    H2 = int(input("Cuanto cuesta H2? ")) 
    print("el valor de Hamburgesa 1 es $",H1)
    print("el valor de Hamburgesa 2 es $",H2)
    return H1,H2

#funcion principal
if __name__ == '__main__':
    H1, H2 = datos()
    print("Hambuergesa 1 es más costosa que Hamburgesa 2? ",compararPrecio(H1, H2))