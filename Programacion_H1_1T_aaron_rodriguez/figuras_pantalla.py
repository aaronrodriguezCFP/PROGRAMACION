#CUESTIÓN 1 
#Función para mostrar el menú de opciones al usuario
def mostrar_menu():
    print("\n Dime una opción:")
    print("1 - Cuadrado") #Opción para calcular el cuadrado
    print("2 - Rectángulo") #Opción para calcular el rectángulo
    print("3 - Salir") #Opción para salir del programa

#Función para calcular y mostrar la figura seleccionada (cuadrado o rectángulo)
def calcular_figura(opcion):
    if opcion == 1: #Si el usuario elige el cuadrado
        lado = int(input("Dime el lado del cuadrado:\n> ")) #Pedir el lado del cuadrado
        area = lado ** 2 #Calcular el área del cuadrado
        perimetro = 4 * lado #Calcular el perímetro del cuadrado
        figura = '* ' * lado #dibujar el cuadrado
        print(("\n" + figura + "\n") * lado, end='') #Imprimir el cuadrado
    
    else: #Si el usuario elige el rectángulo
        base = int(input("Dime la base del rectángulo:\n> ")) #Pedir la base del rectángulo
        altura = int(input("Dime la altura del rectángulo:\n> ")) #Pedir la altura del rectángulo
        area = base * altura #Calcular el área del rectángulo
        perimetro = 2 * (base + altura) #Calcular el perímetro del rectángulo
        figura = '* ' * base #dibujar el rectángulo
        print(("\n" + figura + "\n") * altura, end='') #Imprimir el rectángulo

    #Mostrar el resultados al usuario 
    print (f"Su área es {area}")
    print (f"Su perímetro es {perimetro}")


##PROGRAMA PRINCIPÂL
while True:#Bucle que permite repetir el menú hasta que el usuario decida salir
    mostrar_menu() #Mostrar el menú de opciones 
    opcion = int(input("> ")) #Leer la opción elegida por el usuario

    if opcion in (1, 2): #Si la opción es 1 o 2 (cuadrado o rectángulo) damos paso a la operación
        calcular_figura(opcion)
    elif opcion == 3: #Si la opción es 3 (salir) ejecutamos la salida del programa con el siguiente print
        print("Saliendo...")
        break
    else : #Si la opción no es válida, mostramos un mensaje de error y volvemos al menú de opciones
        print("Opción no válida. Intente de nuevo.")

