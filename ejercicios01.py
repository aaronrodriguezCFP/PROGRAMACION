#calculadora
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
operacion = input("Ingrese la operación, suma, resta, multiplicacion o division: ")

if operacion == "suma":
    resultado1 = numero1 + numero2
    print("El resultado de la suma es:", resultado1)
elif operacion == "resta":
    resultado2 = numero1 - numero2
    print("El resultado de la resta es:", resultado2)
elif operacion == "multiplicacion":
    resultado3 = numero1 * numero2
    print("El resultado de la multiplicacion es:", resultado3)
elif operacion == "division":
    if numero2 == 0:
        print("No se puede dividir por cero")
    else:
        resultado4= numero1 / numero2
        print("El resultado de la division es:", resultado4)


#numero par e impar 
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")


#Suma de los N primeros numeros
n = int(input("Ingrese un número entero positivo: "))
if n >= 0 :
    suma = 0
    for i in range(1, n+1):
        suma = suma + i
    print("La suma de los", n, "primeros numeros es:", suma)
else:
    print("El número debe ser positivo")


#Contador de vocales
palabra = input("Ingrese una palabra: ")
contador = 0
for i in palabra:
    if i in "aeiouAEIOU":
        contador = contador + 1
print("La palabra", palabra, "tiene", contador, "vocales")


#Adivina el número
import random
numero = random.randint(1, 100)

adivinado = False

print("Adivina el número")

while not adivinado:
    intentar = int(input("prueba otra vez"))
    if intentar < numero:
        print("Es menor")
    elif intentar > numero:
        print("Es mayor")
    else:
        print("Es correcto")
        adivinado = True
