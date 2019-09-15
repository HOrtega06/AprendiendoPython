for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
    #print sin argumentos es un salto de linea
    print()
    for j in range(1,11):
        #Aqui i contiene el numero base de la tabla
        #y j el elemento de la tabla
        salida="{} x {} = {}"
        print(salida.format(i,j,i*j))
    else:
        #Al concluir con las iteraciones indicadas
        #se ejecuta este codigo, que es un salto de linea
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