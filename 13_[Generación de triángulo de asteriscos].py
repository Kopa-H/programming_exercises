### Triángulo de asteriscos ###

"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla 
un triángulo rectángulo como el de más abajo, de altura el número introducido.
"""

number = int(-1)

while number < 0:
    try:
        number = int(input("Por favor, introduzca su número entero positivo: "))
    except:
        print("¡Solo aceptamos números positivos enteros!")

def triangulación():
    for i in range(number):
        for j in range(i+1):
            print("*", end= "")
        print("")

    
triangulación()
