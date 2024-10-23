
#contador de numeros pares 
numero = int(input("Introduce un número entero positivo: "))
if numero > 0:
    contador = 0
    for i in range(1, numero + 1):
        if i % 2 == 0:
            contador += 1
    print(f"Hay {contador} números pares entre 1 y {numero}.")
else:
    print("Error: Debes introducir un número entero positivo.")



#Suma de números hasta que se introduce un negativo
suma_total = 0 
while True:
    numero = int(input("introduce un numero entero (o un numero negativo para terminar): "))
    if numero < 0:
        break
    else:
        suma_total = suma_total + numero
    print(f"La suma de los numeros positivos introducidos es: {suma_total}")



#Tabla de multiplicar 
numero = int(input("Ingrese un numero entero positivo: "))
if numero > 0:
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
else:
    print("Error: Debes introducir un número entero positivo.")



#Adivinar un número
import random
numero_secreto = random.randint(1,100)

print ("Adivina el numero secreto entre 1 y 100")

while True:
    numero = int(input("introduce un numero entre 1 y 100: "))
    if numero > numero_secreto:
        print("Es menos")
    if numero < numero_secreto:
        print("Es más")
    if numero == numero_secreto:
        print("Es correcto")
        break



#contar vocales en una palabra
palabra = input("introduce una palabra:")
contador_vocales = 0
vocales = "aeiouAEIOU"
for i in palabra:
    if i in vocales:
        contador_vocales += 1
print(f"La palabra {palabra} tiene {contador_vocales} vocales")
