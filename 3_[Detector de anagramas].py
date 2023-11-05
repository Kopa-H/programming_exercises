### Detector de anagramas ###

"""
Escribe una función que reciba dos palabras (str) y retorne
True o False según sean o no anagramas.
- Un anagrama consiste en formar una palabra reordenando TODAS sus
letras de otra palabra original.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no se consideran un anagrama.
"""

first_word = input("Introduzca su primera palabra:")
second_word = input("Por favor, ahora introduzca su segunda palabra:")
print("Muchas gracias. Ahora, por favor, espere.")
print("...") 
print("...")
print("...")

def anagram_detecter(first_word, second_word):
    if first_word.lower() == second_word.lower():
        print("Ambas palabras son iguales. Ello no se considera un anagrama. \nPor favor, recargue la página para volver a intentarlo ;)")
        return False
    if sorted(first_word.lower()) == sorted(second_word.lower()):
        print("¡Ambas palabras forman un anagrama!")
        return True
    else:
        print("¡Ambas palabras NO forman un anagrama!")

anagram_detecter(first_word, second_word)