### Contraseña ###

"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""

password = input("Introduce your password: ")
repeated_password = str

try:
    while repeated_password != password:
        repeated_password = input("Please, introduce your password again: ")
        while repeated_password != password:
            print("Passwords do not match")
            repeated_password = input("Please, introduce your password again: ")
finally:
    print("\033[1m" + "¡Your password has been changed!" + "\033[0m")
