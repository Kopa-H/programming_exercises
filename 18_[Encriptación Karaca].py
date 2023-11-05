"""
 * Crea una función que sea capaz de encriptar y desencriptar texto utilizando el algoritmo de encriptación de Karaca. 
"""
from termcolor import cprint
import time
import keyboard

class Karaca:
    def __init__(self, clave_descifrado, tabla):
        self.clave_descifrado = clave_descifrado
        self.tabla = tabla
    
    def encriptar(self, texto):
        texto_cifrado = ""
        for letra in texto:
            if letra in self.tabla:
                texto_cifrado += self.tabla[letra] #Se accede al valor de la letra original (que es la key) y se suma a la string mensaje_cifrado.
            else:
                texto_cifrado += letra #Por si acaso esa misma letra no existe en el diccionario pasado al objeto, entonces se añade tal cual está.
        return texto_cifrado

    def desencriptar(self,texto_cifrado):
        tabla_inversa = {value: key for key, value in self.tabla.items()} #Con esto creamos el diccionario inverso invirtiendo los valores y las keys del diccionario ya creado.
        texto_descifrado = ""
        for letra in texto_cifrado:
            if letra in tabla_inversa:
                texto_descifrado += tabla_inversa[letra] #Se accede al valor de la letra original (que es la key) y se suma a la string mensaje_cifrado.
            else:
                texto_descifrado += letra #Por si acaso esa misma letra no existe en el diccionario pasado al objeto, entonces se añade tal cual está.
        return texto_descifrado
objeto_karaca = Karaca(input("Registre su contraseña de descifrado: "), {
    "A" : "B",
    "B" : "C",
    "C" : "D",
    "D" : "E",
    "E" : "F",
    "F" : "G",
    "G" : "H",
    "H" : "I",
    "I" : "J",
    "J" : "K",
    "K" : "L",
    "L" : "M",
    "M" : "N",
    "N" : "Ñ",
    "Ñ" : "O",
    "O" : "P",
    "P" : "Q",
    "Q" : "R",
    "R" : "S",
    "S" : "T",
    "T" : "U",
    "U" : "V",
    "V" : "W",
    "W" : "X",
    "X" : "Y",
    "Y" : "Z",
    "Z" : "A",
    "a" : "b",
    "b" : "c",
    "c" : "d",
    "d" : "e",
    "e" : "f",
    "f" : "g",
    "g" : "h",
    "h" : "i",
    "i" : "j",
    "j" : "k",
    "k" : "l",
    "l" : "m",
    "m" : "n",
    "n" : "ñ",
    "ñ" : "o",
    "o" : "p",
    "p" : "q",
    "q" : "r",
    "r" : "s",
    "s" : "t",
    "t" : "u",
    "u" : "v",
    "v" : "w",
    "w" : "x",
    "x" : "y",
    "y" : "z",
    "z" : "a",

    "á" : ";",
    "é" : "€",
    "í" : "·",
    "ó" : "¨",
    "ú" : "&",

    "?" : "(",
    "¿" : "$",
    "." : "#",
    "," : "|",
    " " : "*"
})

texto_a_encriptar = "El destino de los hombres está hecho de momentos felices, toda la vida los tiene, pero no de épocas felices. Sin arte la vida sería un error. ¿No es la vida cien veces demasiado breve para aburrirnos? El mundo real es mucho más pequeño que el mundo de la imaginación."

def cifrar_texto():
    print("Para cifrar su texto, pulse la tecla [C]")
    key = ""
    while key.lower() != "c":
        key = keyboard.read_key()
        if key.lower() == "c":
            texto_cifrado = objeto_karaca.encriptar(texto_a_encriptar)
            print("...\nCifrando texto\n...")
            time.sleep(5)
            cprint(text="Texto cifrado:\n", on_color="on_red", end="") 
            print(texto_cifrado.lower())
            return texto_cifrado
def descifrar_texto():
    texto_cifrado = cifrar_texto()
    key=""
    clave_descifrado=""
    print("\nPara descifrar su texto, pulse la tecla [D]")
    while key.lower() != "d":
        key = keyboard.read_key()
        if key.lower() == "d":
            while clave_descifrado != objeto_karaca.clave_descifrado:
                clave_descifrado = input("Introduzca su contraseña de descifrado: ")
                if clave_descifrado == objeto_karaca.clave_descifrado:
                    print("...\nDescifrando texto\n...")
                    time.sleep(5)
                    texto_descifrado = objeto_karaca.desencriptar(texto_cifrado)
                    cprint(text="Texto descifrado:\n", on_color="on_green", end="")
                    print(texto_descifrado)
                else:
                    cprint(text="¡La contraseña es incorrecta!", color="red")
descifrar_texto()