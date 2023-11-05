### Ejercicios vídeo de Mouredev ###

#El famoso FIZZ BUZZ#

"""
Escribe un program que muestre por consola los números
de 1 a 100 (amnps incluidos y con un salto de línea entre cada impresión)
sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y 5 por la palabra "fizzbuzz"
"""

def fizzbuzz_function():
    for i in range(1, 101):
        if i % 3 == 0: #Que i % 3 significa que no existe residuo entre la división de ambos números. De ahí que se haga así.
            print("fizz")
        if i % 5 == 0:
            print("buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        else:    
            print(i)

fizzbuzz_function() #Con esto ya estaríamos
