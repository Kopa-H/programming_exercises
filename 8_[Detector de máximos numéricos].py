### Detector de máximos numéricos en lista ###

def max_numbers_in_list(numbers):
    while True:
        try:
            number = float(input("Introduzca su número: "))
        except ValueError:
            print("Por favor, introduzca un valor numérico.")
        else:
            numbers.append((number))
            print("Su lista actual es:", numbers)
            close = input("¿Desea añadir más valores? \n>>>Escriba Sí/No: ")
            if close.lower() == "no":
                return False, print("El número más grande de su lista es:", (max(numbers)))

max_numbers_in_list(numbers = [])