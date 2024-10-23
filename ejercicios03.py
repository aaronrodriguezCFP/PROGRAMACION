#Lista de reproducción musical
lista_reproduccion = []

while True:
    cancion = input("Ingresa el nombre de la canción (o 'fin' para terminar): ")
    if cancion.lower() == "fin":
        break
    lista_reproduccion.append(cancion)

print("\nTu lista de reproducción:")
for i, cancion in enumerate(lista_reproduccion, start=1):
    print(f"{i}. {cancion}")
indice = int(input("\nIngresa el número de la canción que quieres reproducir: ")) - 1

if 0 <= indice < len(lista_reproduccion):
    print(f'Reproduciendo "{lista_reproduccion[indice]}"...')
else:
    print("Número de canción no válido.")


#Agenda de contactos
contactos = []
while True:
    nombre = input("Ingresa el nombre del contacto (o 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    telefono = input(f"Ingresa el número de teléfono del contacto {nombre}: ")
    contactos[nombre] = telefono

print("\nTu agenda de contactos:")
for nombre, telefono in contactos.items():
    print(f"{nombre}: {telefono}")

nombre_buscar = input("\nIngresa el nombre del contacto que deseas buscar: ")
if nombre_buscar in contactos:
    print(f"El número de teléfono del contacto {nombre_buscar} es {contactos[nombre_buscar]}.")
else:
    print(f"No se encontró el contacto {nombre_buscar}.")


#Planificación de viaje 
itinerario = ("Madrid", "Barcelona", "Valencia", "Sevilla")

print("Itinerario de viaje:")
for i, ciudad in enumerate(itinerario, start=1):
    print(f"{i}. {ciudad}")

posicion = int(input("\nIngresa la posición para saber qué ciudad visitarás: ")) - 1

if 0 <= posicion < len(itinerario):
    print(f"En la posición {posicion + 1} visitarás: {itinerario[posicion]}.")
else:
    print("Posición no válida. Por favor, ingresa un número entre 1 y", len(itinerario) + 1)


#Registro de calificaciones
calificaciones = {}

while True:
    asignatura = input("Ingresa el nombre de la asignatura (o 'fin' para terminar): ")
    if asignatura.lower() == "fin":
        break
    try:
        calificacion = float(input(f"Ingresa la calificación de {asignatura}: "))
        calificaciones[asignatura] = calificacion
    except ValueError:
        print("Por favor, ingresa una calificación válida.")

print("\nResumen de calificaciones:")
for asignatura, calificacion in calificaciones.items():
    print(f"- {asignatura}: {calificacion}")

if calificaciones:
    media = sum(calificaciones.values()) / len(calificaciones)
    print(f"\nCalificación media: {media:.2f}")
else:
    print("No se ingresaron calificaciones.")


#Menú de cafetería
menu = {
    "Café": (1.5, 50),
    "Té": (1.0, 0),
    "Bocadillo": (3.0, 300),
    "Ensalada": (2.5, 150)
}

print("Menú:")
for producto, (precio, calorias) in menu.items():
    print(f"- {producto}: {precio}€ ({calorias} cal)")

pedido = []
total_precio = 0
total_calorias = 0

while True:
    producto_seleccionado = input("Ingresa el nombre del producto que deseas agregar (o 'fin' para terminar): ")
    
    if producto_seleccionado.lower() == "fin":
        break
    
    if producto_seleccionado in menu:
        precio, calorias = menu[producto_seleccionado]
        pedido.append(producto_seleccionado) 
        total_precio += precio  
        total_calorias += calorias  
    else:
        print("Producto no disponible en el menú. Intenta de nuevo.")

print("\nTu pedido:")
for item in pedido:
    print(f"- {item}")

print(f"\nTotal a pagar: {total_precio:.2f}€")
print(f"Calorías totales: {total_calorias} cal")
