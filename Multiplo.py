numero=int(input("Ingrese un numero entero: "))
#Aqui podemos ver que si el residual es 0 quiere decir que 
#el numero ingresado es multiplo
esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)
#con and es verdadero si todas las condiciones son verdaderas,
#con or es verdadero cuando al menos una conficion lo es.
#()juntar o solo.
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
