# Carga de Datos:
# Crea una lista de diccionarios llamada ventas, donde cada diccionario represente una venta. Cada venta debe incluir las siguientes claves:
# «fecha»: una cadena de texto que represente la fecha de la venta (por ejemplo, «2026-04-04»).👌
# «producto»: una cadena de texto que represente el nombre del producto vendidos.👌
# «cantidad»: un número entero que represente la cantidad de productos vendidos.👌
# «precio»: un número flotante que represente el precio unitario del producto.👌
# Cálculo de Ingresos Totales:
# Utiliza un bucle para iterar sobre la lista ventas y calcular los ingresos totales generados por todas las ventas. Los ingresos totales se calculan multiplicando la cantidad vendida por el precio unitario para cada venta y sumando los resultados.👌
# Análisis del Producto Más Vendido:
# Crea un diccionario llamado ventas_por_producto donde las claves sean los nombres de los productos y los valores sean la cantidad total vendida de cada producto.👌
# Utiliza este diccionario para identificar el producto que tuvo la mayor cantidad total vendida.
# Promedio de Precio por Producto:
# Crea un diccionario llamado precios_por_producto donde las claves sean los nombres de los productos y los valores sean tuplas. Cada tupla debe contener dos elementos: la suma de los precios de venta de todas las unidades vendidas y la cantidad total de unidades vendidas.
# Calcula el precio promedio de venta para cada producto utilizando la información de este diccionario.
# Ventas por Día:
# Crea un diccionario llamado ingresos_por_dia donde las claves sean las fechas y los valores sean los ingresos totales generados en cada día.
# Utiliza un bucle para calcular los ingresos totales por día y almacenar estos valores en el diccionario.
# Representación de Datos:
# Crea un diccionario llamado resumen_ventas donde las claves sean los nombres de los productos y los valores sean diccionarios anidados. Cada diccionario anidado debe contener:
# «cantidad_total»: la cantidad total vendida del producto.
# «ingresos_totales»: los ingresos totales generados por la venta del producto.
# «precio_promedio»: el precio promedio de venta del producto.
 

# Entrega: Presenta tus resultados en un archivo de texto o una hoja de cálculo. Detalla cada paso del análisis y los resultados obtenidos. Asegúrate de incluir:

# La lista de ventas original.
# Los ingresos totales generados.
# El producto más vendido y su cantidad total vendida.
# El precio promedio de venta por producto.
# Los ingresos totales por día.
# El resumen de ventas por producto.

import re

ventas_por_producto = {}

ventasAbril = [
    {"fecha": "2026-04-15", "producto": "Camiseta", "cantidad": 10, "precio": 19.999},
    {"fecha": "2026-04-15", "producto": "Pantalón Vaquero", "cantidad": 5, "precio": 39.999},
    {"fecha": "2026-04-15", "producto": "Zapatos Deportivos", "cantidad": 8, "precio": 49.999},
    {"fecha": "2026-04-16", "producto": "Camiseta", "cantidad": 7, "precio": 19.999},
    {"fecha": "2026-04-16", "producto": "Pantalón Vaquero", "cantidad": 3, "precio": 39.999},
    {"fecha": "2026-04-16", "producto": "Zapatos Deportivos", "cantidad": 4, "precio": 49.999},
    {"fecha": "2026-04-17", "producto": "Camiseta", "cantidad": 12, "precio": 19.999},
    {"fecha": "2026-04-17", "producto": "Pantalón   Vaquero", "cantidad": 6, "precio": 39.999},
    {"fecha": "2026-04-17", "producto": "Zapatos Deportivos", "cantidad": 10, "precio": 49.999}
]

def ingresosTotales(ventasMes):
    total = 0
    for venta in ventasMes:
        total += venta["cantidad"] * venta["precio"]
    return print(f"Ingresos Totales: {total}")

ingresosTotales(ventasAbril)

def ventasporPorducto(ventasMes):
    for venta in ventasMes:
        producto = venta["producto"]
        cantidad = venta["cantidad"]
        if producto in ventas_por_producto:
            ventas_por_producto[producto] += cantidad
        else:
            ventas_por_producto[producto] = cantidad
    return print(f"Ventas por Producto: {ventas_por_producto}")

def mayorCantidadVendida(ventas_por_producto):
    producto = max(ventas_por_producto, key=ventas_por_producto.get)
    cantidad = ventas_por_producto[producto]
    return print(f"Producto más vendido: {producto}, Cantidad total vendida: {cantidad}")

ventasporPorducto(ventasAbril)
mayorCantidadVendida(ventas_por_producto)
