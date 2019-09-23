entrada=input()
print(type(entrada))
esEntero=(entrada.isdigit() and entrada.find(".")==-1)
if (esEntero):
    print("Dato entero. ¡Muy bien!.")
else:
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
