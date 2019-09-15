#python posee muchas librerias listas para utilizarse.
#A dichas librerias se les da el nombre de modules (module),
#para utilizar un modulo en un programa, primero debe
#importarse, usando la instruccion import
import random

#Se define variable (float) y se le asiga valor
num1=float(10.5)

#Una funcion es un conjunto de intrucciones que procesan
#una tarea especifica, como una unidad de ejecucion.
#Se declara con (def). Todo el codigo posicionado a la derecha
#de la definicion (identado), forma parte de la funcion.
def FunRandom():
    #Se convierte a float el numero aleatorio generado por
    #random.randrange() (solo esta disponible si se importa
    # el modulo random)
    num2=float(random.randrange(1,10))
    #Se utilizan meta sustituciones para mostrar resultados
    mensaje="La suma de {} y {} es {}"
    #({}=num1, {}=num2, {}=num1+num2)
    print(mensaje.format(num1,num2,num1+num2))

#Finalmente se ejecuta la funcion en el codigo
FunRandom()

#Elaboramos un programa que declare una variable global de tipo float
#asignandole un valor cualquiera, explicitamente float; y despues
#elaboramos un funcion (def) que declare una variable local de tipo float,
#que adquiera un valor aleatorio entre el 1 y 10, y que muestre en consola
#el resultado de la suma de las dos variables, usando el mensaje "La suma
#de x and y es z". Usamos import, float(), def y str.format
#Entradas y salidas:
#La suma de 10.5 y 2.5 es 13.00
