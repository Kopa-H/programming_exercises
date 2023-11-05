### Notas ordenadas ###

"""Escribir una función que reciba un diccionario con las notas de los alumnos de un curso 
y devuelva una serie con las notas de los alumnos aprobados ordenadas de mayor a menor.

Se supone que debería hacerse utilizando la librería Pandas, pero honestamente me da todo el palo ahora mismo investigar cómo mierda funciona, así que lo haré sin nada.
"""
import random
import matplotlib.pyplot as plt
from termcolor import cprint

def generar_notas():
  rng = random.Random() #Generador de números aleatorios
  dni_y_notas = {}
  
  for _ in range(50):
    letra_dni = chr(rng.randint(ord('A'), ord('Z'))) #Generamos una letra al azar para añadirla a las keys.
    dni = str(rng.randint(10000000, 99999999)) + letra_dni
    nota = rng.randint(0, 10)
    dni_y_notas[dni] = nota #Syntaxis importante! Estamos asignando el valor de la variable nota a la clave dni del diccionario dni_y_notas.
  
  return dni_y_notas

def clasificar_notas():
  dni_y_notas = generar_notas() #Obtenemos el diccionario random de DNIs y notas.
  global solo_notas, notas_aprobadas

  # Crea una lista de tuplas con la clave y el valor del diccionario
  notas_ordenadas = []
  solo_notas = []
  for dni, nota in dni_y_notas.items():
    notas_ordenadas.append((dni, nota))
    solo_notas.append(nota)
  notas_ordenadas.sort(key=lambda x: x[1], reverse=True) #Con lo de lambda x: x[1] especificamos que queremos ordenar la lista mediante el valor de las notas.

  notas_aprobadas = 0

  for dni, nota in notas_ordenadas:
    if nota >= 5:
      print(f"El alumno", dni, "tiene una nota de", end=" ") 
      cprint(text=nota, on_color="on_green",end="\n")
      notas_aprobadas += 1
    elif nota < 5:
      print(f"El alumno", dni, "tiene una nota de", end=" ") 
      cprint(text=nota, on_color="on_red", end="\n")

def mostrar_notas():
  global media_aritmetica
  suma_notas = sum(solo_notas)
  tamaño_notas = len(solo_notas)
  media_aritmetica = suma_notas / tamaño_notas #Calculamos la media de las notas.
  porcentaje_aprobados = (notas_aprobadas / tamaño_notas) * 100
  print(f"La media de la clase ha sido de", media_aritmetica)
  print(f"El", int(porcentaje_aprobados), "%", "de vosotros habéis aprobado el examen.")

def mostrar_grafico():
    plt.figure(figsize=(7, 5), dpi=150) #Con esto ajustamos el tamaño de la ventana que vamos a crear, sobre la cual se establecerá el gráfico.
    plt.hist(solo_notas, histtype="bar", edgecolor="black") #Creamos el histograma dentro de la ventana.
    plt.title("Distribución de las notas") #Le ponemos leyenda.
    plt.axvline(media_aritmetica, color="red", linestyle="dashed", linewidth=2) #Dibujamos la línea roja de la media.
    
    plt.xticks(range(0, 11, 1)) #Establecemos valores de 0 a 10 con un intervalo de 1.
    plt.yticks(range(0, 11, 1)) #De este modo expresamos el porcentaje.

    plt.text(0.05, 0.7, "Eje Y: Frecuencia", ha="left", va="top", rotation=90, transform=plt.gcf().transFigure, fontsize=14)
    plt.text(0.41, 0.05, "Eje X: Notas", ha="left", va="top", transform=plt.gcf().transFigure, fontsize=14)
    
    plt.annotate(
    "Media aritmética",  # Texto de la anotación
    xy=(media_aritmetica, 7),  # Posición del punto al que se conecta la anotación
    xytext=(media_aritmetica + 2, 7),  # Posición del texto de la anotación
    arrowprops=dict(facecolor='red', edgecolor='red', linewidth=2),  # Propiedades de la flecha que conecta la anotación con el punto
    ha="center",  # Alineación horizontal del texto
    fontsize=11)  # Tamaño del texto
    
    plt.show()

clasificar_notas()
mostrar_notas()
mostrar_grafico()