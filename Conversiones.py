#Declaramos una cadena
numero = "1234"
# type = da un dato type, no un str(<class 'str'>).
print(type(numero))
#Convertimos la cadena a int.
numero=int(numero)
#Cambiamos el tipo de la variable auqnue esta
#siga siendo la misma(<class 'int'>).
print(type(numero))
#Usamos meta sustitucion
#format se usa para dar posiscion a valores
salida="El numero utilizado es {}"
print(salida.format(numero))

#Declaramos una variable de tipo str con un valor de "1234", y mostramos
#el data type de la variable: realizamos la conversion del dato a int, y
#mostramos el nuevo data type.
#Entradas y salidas:
# <class'str'>
# <class'int'>
# El numero utilizado es 1234
