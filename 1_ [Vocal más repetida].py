### Reto n.47: VOCAL MÁS COMÚN ###

"""
Enunciado:
- Crea una función que reciba un texto y retorne la vocal que más veces se repita.
- Ten cuidado con algunos casos especiales.
- Si no hay vocales podrá devolver vacío. 
"""

def vocal_counter_a(my_text):
    vocal_a = "a"
    return [character for character in my_text if character in vocal_a]

def vocal_counter_e(my_text):
    vocal_e = "e"
    return [character for character in my_text if character in vocal_e]

def vocal_counter_i(my_text):
    vocal_i = "i"
    return [character for character in my_text if character in vocal_i]

def vocal_counter_o(my_text):
    vocal_o = "o"
    return [character for character in my_text if character in vocal_o]

def vocal_counter_u(my_text):
    vocal_u = "u"
    return [character for character in my_text if character in vocal_u]

my_text = input('Por favor, introduzca su texto a continuación:')

print("a=", len((vocal_counter_a(my_text))))
print("e=", len((vocal_counter_e(my_text))))
print("i=", len((vocal_counter_i(my_text))))
print("o=", len((vocal_counter_o(my_text))))
print("u=", len((vocal_counter_u(my_text))))

number_of_a = len((vocal_counter_a(my_text)))
number_of_e = len((vocal_counter_e(my_text)))
number_of_i = len((vocal_counter_i(my_text)))
number_of_o = len((vocal_counter_o(my_text)))
number_of_u = len((vocal_counter_u(my_text)))
print(type(number_of_a))

winning_a = number_of_a > number_of_e and number_of_a > number_of_i and  number_of_a > number_of_o and number_of_a > number_of_u
winning_e = number_of_e > number_of_i and number_of_e > number_of_a and  number_of_e > number_of_o and number_of_e > number_of_u
winning_i = number_of_i > number_of_a and number_of_i > number_of_e and  number_of_i > number_of_o and number_of_i > number_of_u
winning_o = number_of_o > number_of_a and number_of_o > number_of_e and  number_of_o > number_of_i and number_of_o > number_of_u
winning_u = number_of_u > number_of_a and number_of_u > number_of_e and  number_of_u > number_of_i and number_of_u > number_of_o

if winning_a == False and winning_e == False and winning_i == False and winning_o == False and winning_u == False:
        print("¡No ha habido ningún ganador!")

for element in my_text:
    if winning_a == True:
        print("¡La letra A gana!")
    if winning_a == True:
        break

    if winning_e == True:
        print("¡La letra E gana!")
    if winning_e == True:
        break

    if winning_i == True:
        print("¡La letra I gana!")
    if winning_i == True:
        break

    if winning_o == True:
        print("¡La letra O gana!")
    if winning_o == True:
        break

    if winning_u == True:
        print("¡La letra U gana!")
    if winning_u == True:
        break  


