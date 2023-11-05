"""
Escribir una función que aplique el IVA a un precio. Escribir una segunda función
que reciba un diccionario con los precios y porcentajes de una cesta de la compra,
y utilice la función para aplicar el IVA a los productos de la cesta y devolver
el precio final de la cesta.
"""

productos = {"Pan": 1.20, "Coca-Cola" : 2.00, "Productos cárnicos" : 12.99, "Tabla de quesos" : 6.22}
precio = 0

def aplicacion_iva(precio):
    precio = precio + ((precio / 100) * 21)
    #print("El precio después de aplicarle el IVA es de " + str(precio) + "€.")
    return precio


def dict_con_iva(productos):
    for producto in productos:
        if producto == int:
            aplicacion_iva(producto)
    return {productos.append(producto)}



aplicacion_iva(precio)
dict_con_iva(productos)
