entrada=input()
print(type(entrada))
#La variable booleana contiene el resultado de verificar si lo
#capturado es digito, y si no se encuentra un punto en lo capturado,
#lo que indicaria que trata de un numero con decimales, es decir un float.
#Si find retorna -1 quiere decir que lo buscado, en este caso es True,
#igual a que lo capturado es entero
esEntero=(entrada.isdigit() and entrada.find(".")==-1)
if (esEntero):
    #Se ejecutara si la condicion es verdadera(True)
    print("Dato entero. ¡Muy bien!.")
else:
    #Se ejecutara si la condicion es falsa(False)
    print("Dato no es entero. Intentar nuevamente.")

#Elaboramos un programa que declare una variable que reciba un valor;
#muestre el data type capturado. Si el valor capturado es integer(es
#digito y no contiene punto ejem:"5"), mostrar la leyenda "Dato
#entero. ¡Muy bien!" o de lo contario, mostrar "Dato no es entero.
#Intentar nuevamente"
# Entradas y salidas:
# 12
# <class 'str'>
# Dato entero. ¡Muy bien!
