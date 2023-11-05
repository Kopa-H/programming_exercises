### Par o impar ###

def par_o_impar():
    if number % 2:
        print("¡Enhorabuena, su número es impar!")
        return True
    if not number % 2:
        print("¡Enhorabuena, su número es par!")
        return False

number = ""

while type(number) != int: #Con este bucle preguntamos el número y evitamos strings sin que el código reviente.
    try:
        number = int(input("Por favor, introduzca un número entero: "))
    except:
        print("¡Solo aceptamos números enteros!")

par_o_impar()
