"""
Escribir un programa que pida al usuario una palabra y luego muestre por
pantalla una a una las letras de la palabra introducida empezando por la última.
"""
     
def reverse(text):    
    text_reversed = text[::-1]
    for i in text_reversed:
        print(i)

reverse(str(input("Escriba su palabra: ")))

"""
Lo mismo pero con una lista.
"""

def reverse(list):  
    for word in list:
        word_reversed = word[::-1]
        for characther in word_reversed:
            print(characther)

list = ["nam yM" " sartneucne et omóC? " ".senoicnuf ed nóicnuf anu se otsE"]
reverse(list)
