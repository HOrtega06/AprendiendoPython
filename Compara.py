numero1=input("Numero 1: ")
numero2=input("Numero 2: ")
salida=("Los numeros proporcionados {} y {}. {}.")
if (numero1==numero2):
    #de ser iguales los numeros aqui entrarian
    print(salida.format(numero1, numero2, "Los numeros son iguales"))
else:
    #Aqui las condicionales son anidadas.
    #Si los numeros no son iguales.
    if numero1>numero2:
        print(salida.format(numero1, numero2, "El mayor es el primero"))
    else:
        print(salida.format(numero1, numero2, "El mayor es el segundo"))

#Elaboramos un programa que pregunte dos numeros, y que muestre cual de los dos
#es mayor, el primero o segundo. Tambien debe reportar si son iguales. El mensaje
#debe decir: “Números proporcionados: x y y. El mayor es primero.” (o el segundo,
# o son iguales, según sea el caso).
#Entradas y salidas:
#Número 1:10
#Número 2:10
#Números proporcionados: 10 y 10, 11 y 10, 10 y 11
#A) Los números son iguales.
#B) El mayor es el primero.
#C) El mayor es el segundo.
