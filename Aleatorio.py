#para utilizar un modulo en un programa, primero debe
#importarse, usando la instruccion import
import random

#La variable la deblaramos como float y con un valor especifico.
num1=float(10.5)

def FunRandom():
    #Ya con el modulo random importado para usarse, se genera un numero aleatorio
    #y de type float.
    num2=float(random.randrange(1,10))
    #Usamos metasustitucion
    mensaje="La suma de {} y {} es {}"
    #({}=num1, {}=num2, {}=num1+num2)
    print(mensaje.format(num1,num2,num1+num2))

FunRandom()

#Elaboramos un programa que declare una variable global de tipo float
#asignandole un valor cualquiera, explicitamente float; y despues
#elaboramos un funcion (def) que declare una variable local de tipo float,
#que adquiera un valor aleatorio entre el 1 y 10, y que muestre en consola
#el resultado de la suma de las dos variables, usando el mensaje "La suma
#de x and y es z". Usamos import, float(), def y str.format
#Entradas y salidas:
#La suma de 10.5 y 2.5 es 13.00
