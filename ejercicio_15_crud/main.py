from categoria_crud import crear_categoria, leer_categorias, actualizar_categoria, eliminar_categoria

def mostrar_menu():
    # Muestra el menú principal con las distintas opciones para gestionar la tabla "categoria"
    print("\nMENU PRINCIPAL")
    print("1. Crear una nueva categoría")
    print("2. Leer todas las categorías")
    print("3. Actualizar una categoría")
    print("4. Eliminar una categoría")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            idcategoria = int(input("Introduzca el ID de la categoría: "))
            nombre = input("Nombre de la nueva categoría: ")
            crear_categoria(idcategoria, nombre)
        elif opcion == "2":
            leer_categorias()
        elif opcion == "3":
            idcategoria = int(input("ID de la categoría a actualizar: "))
            nuevo_nombre = input("Nuevo nombre de la categoría: ")
            actualizar_categoria(idcategoria, nuevo_nombre)
        elif opcion == "4":
            idcategoria = int(input("ID de la categoría a eliminar: "))
            eliminar_categoria(idcategoria)
        elif opcion == "5":
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida")

main()





