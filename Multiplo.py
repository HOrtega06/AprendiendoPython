#Se captura un numero y se almacena una vez que es
# convertido a int
numero=int(input("Ingrese un numero entero: "))
#Se almacenan en valores booleanos la evaluacion
#de residuales. Si el residual es cero, quiere decir
#que el numero es multiplo
esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)
#Cuando se usa and, se resuelve por verdadero si todas
#las condiciones son verdaderas. Cuando se usa or, se
#resuelve por verdadero si al menos una condicion es
#verdadera. Los parentesis le dicen a python que
#las primeras dos condiciones son juntas, y la tercera
#es independiente.
if((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("Correcto.")
else:
    print("Incorrecto.")

#Elabore un programa que pregunte un numero entero. Si el numero
#es múltiplo de 3 y múltiplo de 5, o múltiplo de 7, muestra el
#el mensaje “Correcto”, de lo contrario, “Incorrecto”. Tip: Si
#un número es múltiplo de otro, módulo es cero.
#Entradas y salidas:
#a) Dame un número entero: 15
# Correcto.
#c) Dame un número entero: 14
# Correcto.
#c) Dame un número entero: 10
# Incorrecto.