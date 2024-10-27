# Pedir saldo inicial 
def solicitar_saldo_inicial():
    saldo = float(input("Introduce un saldo inicial: "))
    while saldo < 0:
        saldo = float(input("El saldo no puede ser negativo. Prueba otra vez: "))
    return saldo

# Función para ingresar dinero
def ingresar_dinero(saldo):
    cantidad = float(input("Cantidad a ingresar: "))
    if cantidad > 0:
        saldo += cantidad
    else:
        print("La cantidad debe ser positiva.")
    return saldo

# Función para retirar dinero
def retirar_dinero(saldo):
    cantidad = float(input("Cantidad a retirar: "))
    if 0 < cantidad <= saldo:
        saldo -= cantidad
    else:
        print("Cantidad no válida.")
    return saldo

# Menú principal
def simulacion_cuenta_bancaria():
    saldo = solicitar_saldo_inicial()
    while True:
        print("Menú de opciones")
        print("1. Ingresar dinero")
        print("2. Retirar dinero")
        print("3. Mostrar saldo")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            saldo = ingresar_dinero(saldo)
        elif opcion == "2":
            saldo = retirar_dinero(saldo)
        elif opcion == "3":
            print(f"Saldo actual: {saldo}€")
        elif opcion == "4":
            print("Adiós")
            break
        else:
            print("Opción no válida.")

#llamamos a la función
simulacion_cuenta_bancaria()


            