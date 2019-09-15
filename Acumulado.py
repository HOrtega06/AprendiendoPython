# Se declaran las variables de trabajo, con tipo explicito.
acumulado=int(0)
numero=str("")

#Al colocar True como condicion de while, se forma
# un ciclo infinito que no se rompera hasta que de
# forma explicita se utilice la instruccion break.
while True:
    numero=input("Dame un numero entero: ")
    if numero=="":
        #Si el numero es vacio, reporta la situacion y sale.
        print("Vacio. Salida del programa.")
        break
    else:
        #Si se proporciono valor, acumulado = acumulado + numero
        #se realiza el calculo usando suma incluyente (+=)
        acumulado+=int(numero)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))

#Elaboramos un programa que pregunye numero enteros indefinidamente
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