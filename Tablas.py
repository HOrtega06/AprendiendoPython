for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
    #salto de linea (print())
    print()
    for j in range(1,11):
        #i tiene la base de la tabla mientras j el elemento de esta misma
        salida="{} x {} = {}"
        print(salida.format(i,j,i*j))
    else:
        #Al acabar con cada iteracion de cada una de las tablas
        #Se hace un salto de linea
        print()

#Crear un programa que elabore las tablas de multiplicar del 1 al 10.
#Cada tabla debera tener un encabezado "Tabla del x". Entre una tabla y otra
#debe haber un salto de linea
#Entradas y salidas:
#Todas las tablas del 1 al 10, pasando espacios
#1 x 1 = 1
#1 x 2 = 2
#1 x 3 = 3
#1 x 4 = 4
#1 x 10 = 10

#Tabla del 2

#2 x 1 = 2
#2 x 2 = 4
#2 x 3 = 6
#2 x 4 = 8
#2 x 10 = 20
