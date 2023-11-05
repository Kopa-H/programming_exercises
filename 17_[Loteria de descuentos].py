"""
Este programa pide primeramente la cantidad total de compras de una persona. Si la cantidad es inferior a $100.00, 
el programa dirá que el cliente no aplica a la promoción. Pero si la persona ingresa una cantidad en compras igual 
o superior a $100.00, el programa genera de forma aleatoria un número entero del cero al cinco. Cada número corresponderá 
a un color diferente de cinco colores de bolas que hay para determinar el descuento que el cliente recibirá como premio. 
Si la bola aleatoria es color blanco, no hay descuento, pero si es uno de los otros cuatro colores, sí se aplicará un 
descuento determinado según la tabla que  aparecerá, y ese descuento se aplicará sobre el total de compra que introdujo 
inicialmente el usuario, de manera que el programa mostrará un nuevo valor a pagar luego de haber aplicado el descuento.
"""

import random
from termcolor import cprint
import time
import keyboard

total_compras = 0
compra_condones = False

print("Sea bienvenido a nuestra nueva promoción, a la que hemos apodado", end=" ")
cprint(text="Lotería de Descuentos de Navidad",attrs=["underline"], end=".\n")

total_compras = int(input("Por favor, antes de nada necesitamos que introduzca el gasto total de su compra: "))

while total_compras < 100:
    print("Sintiéndolo mucho, la cantidad mínima de gasto para probar suerte en nuestra lotería de descuentos es de 100€")
    time.sleep(4)
    print("...")
    print(f"Actualmente su gasto es de {total_compras}€. Se me ocurre algo, señor, si así lo desea puede aumentar su gasto para llegar a los 100€ mediante la compra de condones XS. Si está de acuerdo, pulse la tecla [C]")
    key = ""
    while key != "c":
        key = keyboard.read_key()
        if key.lower() == "c":
            compras_extra = 100 - total_compras
            total_compras += (100 - total_compras)
            time.sleep(6)
            print(f"Gastando {compras_extra}€ en condones XS ha conseguido aumentar su gasto hasta los {total_compras}€.")
            compra_condones = True

print("¡Enhorabuena, su gasto le permite participar en nuestra promoción especial!")
time.sleep(5)
print("         Color                        Descuento")
print("-----------------------------------------------------")
print("      Bola Blanca                     NO TIENE")
print("      Bola Roja                         10%")
print("      Bola Azul                         20%")
print("      Bola Verde                        30%")
print("      Bola Amarilla                     50%")

colores_bolas = {
    1: "bola blanca",
    2: "bola roja",
    3: "bola azul",
    4: "bola verde",
    5: "bola amarilla"
}
numero_random = random.randint(1,5)
bola_color = colores_bolas[numero_random]

time.sleep(5)
print(f"Aleatoriamente, usted ha obtenido una {bola_color}.")

porcentajes_descuento = {
    1: 0,
    2: 10,
    3: 20,
    4: 30,
    5: 50
}
porcentaje_descuento = porcentajes_descuento[numero_random]
precio_final = total_compras - ((total_compras * porcentaje_descuento) / 100)

time.sleep(3)
if numero_random == 1:
    print("Vaya, ¡qué mala suerte!, no podrá gozar de ningún descuento.")
    if compra_condones == True:
        print("Encima tuvo que comprar los condones XS para llegar al gasto mínimo, ¡pobre desdichado!")
    else:
        print("Venga, alégrese, piense que hay fracasados a los que les hacemos comprar condones XS para que lleguen al gasto mínimo para la participación y pierden como usted.")
else:
    print(f"¡Vaya, parece que ha obtenido un {porcentaje_descuento}% de descuento!")
    time.sleep(5)
    print(f"Su gasto final ha pasado de {total_compras}€ a {int(precio_final)}€.")
    if compra_condones == True:
        print("Además, como tuvo que ampliar su gasto, puede llevarse la caja de condones XS.")
        cprint(text="¡Hasta la vista!", color= "red")
            
