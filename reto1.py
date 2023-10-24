#Importaciones de paquetes

#Espacios de funciones y clases

# Colecciones: Son agrupación de valores
# [] lista --> Orden(índices, elementos)
# () Tupla --> Orden
# {} Diccionario --> Conjunto/categoría


#tupla
def calcularPromedioEdad():
    suma = 0
    edades = (51, 39, 23, 39, 25, 21, 37)
    i = 0

    for edad in edades:
     suma = suma + edad
     i = i+1
    promedio = suma/i
    print (f'El promedio es {promedio} años') #string interpolator

#Función principal
if __name__ == '__main__':
    pass