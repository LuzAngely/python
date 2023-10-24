import json
import numpy as np

#(E)xtraer los datos
with open('ventas.json', 'r') as file:
    data = json.load(file)


#(T)ransformar los datos
productos = data['productos']
meses = data['meses']
ventas = data['ventas']

#estadisticas de ventas por producto
ventas_por_producto = {producto: [] for producto in productos}

#estadisticas de ventas por mes
ventas_por_mes = {mes:[] for mes in meses}  #sugar code :: Lamda Programming

#ventas_por_mes2 = {}
#for mes in meses:
#    ventas_por_mes2[mes]=[]

#adicionar las estadisticas
#productos
for producto in productos:
    for anio in ventas[producto].keys():
        for mes in meses:
            ventas_por_producto[producto].append(ventas[producto][anio][mes])
            ventas_por_mes[mes].append(ventas[producto][anio][mes])

#print(ventas_por_producto)
#print('-------------------')
#print(ventas_por_mes)
#input('Any key')

estadistica_por_producto = {}
estadistica_por_mes = {}
#print('====================================')
#print(f'ventas_por_producto.items()= {ventas_por_producto.items()}')
#[( 'Gaseosas',[]),('Crispetas',[]),( 'HotDog',[])]

for producto, ventas in ventas_por_producto.items():
    estadistica_por_producto[producto] = {
        'Promedio': float(np.mean(ventas)),
        'Minimo': int(np.min(ventas)),
        'Maximo': int(np.max(ventas)),
        'Suma': int(np.sum(ventas)),
        'DesviacionEstandar': float(np.std(ventas)),
        'Mediana': float(np.median(ventas))
    }

for mes, ventas in ventas_por_mes.items():
    estadistica_por_mes[mes] = {
        'Promedio': float(np.mean(ventas)),
        'Minimo': int(np.min(ventas)),
        'Maximo': int(np.max(ventas)),
        'Suma': int(np.sum(ventas)),
        'DesviacionEstandar': float(np.std(ventas)),
        'Mediana': float(np.median(ventas))
    }       

with open('estidisticas_por_producto.json', 'w') as file:
    json.dump(estadistica_por_producto, file, indent=4)

with open('estidisticas_por_mes.json', 'w') as file:
    json.dump(estadistica_por_mes, file, indent=4)

print('estadisticas generadas..')