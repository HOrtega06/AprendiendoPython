# Declaramos variables con valor
acumulado=int(0)
numero=str("")

#Con while, se forma un ciclo infinito que no se detendra hasta que se use
#break.
while True:
    numero=input("Dame un numero entero: ")
    if numero=="":
        #Si no hay valor se sale.
        print("Vacio. Salida del programa.")
        break
    else:
        #Si se proporciono valor, acumulado = acumulado + numero
        #se realiza el calculo usando suma incluyente (+=)
        acumulado+=int(numero)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))

#Elaboramos un programa que pregunte numero enteros indefinidamente
#Cada numero que pregunte, debera acumularlo, mostrando "Acumulado
# hasta el momento: x". El programa no deja de preguntar numeros y
# acumularlos, hasta que se deje vacia la entrada.
#Entradas y salidas:
#Dame un número entero: 10
#Monto acumulado: 10
#Dame un número entero: 20
#Monto acumulado: 30
#Dame un número entero:
#Vacío. Salida del programa.
