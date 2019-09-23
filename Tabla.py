numero=input("Dame un numero del 1 al 9: ")
numero=int(numero)

#for es usado para ciclos y se usa con range para repetir un proceso
#el numero de veces que se le asigne al mismo (range, sin contar el limite)
for i in range(1,11):
    # i cambia al iterar repetidas veces
    salida="{} x {} = {}"
    print(salida.format(numero,i,numero*i))

#Elaborar un programa que pregunte un numero entero del 1 al 9, y que
#muestre la tabla de multiplicar del numero proporcionado.
#Entradas y salidas:
#3 x 1 = 3
#3 x 2 = 6
#3 x 3 = 9
#3 x 4 = 12
#3 x .......
#3 x 10 = 30
