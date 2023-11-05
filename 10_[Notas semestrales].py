### Notas de asignaturas ###

"""
Escribir un programa que almacene las asignaturas de un curso en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura, y después las
muestre por pantalla con el mensaje: En <asignatura> has sacado <nota> donde
<asignatura> es cada una des las asignaturas de la lista y <nota> cada una 
de las correspondientes notas introducidas por el usuario.
"""

asignaturas = ["Recursos Humanos", "Marketing", "Estadística I", "EEM", "EEE"]
notas = []

for asignatura in asignaturas:
    nota = input("¿Qué nota has sacado en " + asignatura + "? ")
    notas.append(nota)
for i in range(len(notas)):
    print("En " + asignaturas[i] + " has sacado un " + notas[i] + ".")
