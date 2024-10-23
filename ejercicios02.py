#Invertir una palabra
palabra = input ("Ingrese una palabra: ")
palabra_invertida = ""
for letra in reversed(palabra):
    palabra_invertida += letra
    print(f"la palabra invertida es: {palabra_invertida}")


#Promedio de números hasta que se introduce un cero
suma_total = 0
contador = 0

while True:
    numero = int(input("ingrese un número entero (o 0 para terminar): "))
    if numero == 0:
        break
    suma_total += numero
    contador += 1
if contador > 0:
    promedio = suma_total / contador
    print(f"el promedio es: {promedio}")


#Recolección de nombres
nombres = []
while True:
    nombre = input("ingrese un nombre: ")
    if nombre == "":
        break
    nombres.append(nombre)
print("los nombres ingresados son:")
print(nombres)
print("nombres ingresados uno por uno:")
for nombre in nombres:
    print(nombre)


#verificación de contraseña
contraseña_correcta = "python123"
while True:
    contraseña = input("ingrese la contraseña: ")
    if contraseña == contraseña_correcta:
        print("contraseña correcta")
        break
    else:
        print("contraseña incorrecta")


#Encontrar el número mayor en una lista
numeros = []
while True:
    entrada = input("Introduce un número (o escribe 'hecho' para terminar): ")

    if entrada.lower() == "hecho":
        break
    
    try:
        numero = float(entrada) 
        numeros.append(numero)  
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número o 'hecho'.")

if numeros:
    numero_mayor = numeros[0]
    for numero in numeros:
        if numero > numero_mayor:
            numero_mayor = numero
    print(f"El número mayor ingresado es {numero_mayor}.")
else:
    print("No se ingresaron números.")