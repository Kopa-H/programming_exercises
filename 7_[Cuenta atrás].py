### Cuenta atrás ###

"""
Escribir un programa que pida al usuario un número entero positivo y muestre
por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""

numeros = [] # Creamos una lista.

number = int(-1)

while number < 0:
    try:
        number = int(input("Por favor, introduzca su número entero positivo: "))
    except:
        print("¡Solo aceptamos números positivos enteros!")

number = number + 1

def cuenta_atras(number):
    while number:
        number = number - 1
        numeros.append(number)
    print(numeros)

cuenta_atras(number)