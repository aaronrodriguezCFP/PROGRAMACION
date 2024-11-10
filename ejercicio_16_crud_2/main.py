# main.py
from categoria_crud import crear_categoria, leer_categorias, actualizar_categoria, eliminar_categoria
from producto_crud import crear_producto, leer_productos, actualizar_producto, eliminar_producto

def mostrar_menu_principal():
    # Menú para seleccionar la tabla
    print("\nMENÚ PRINCIPAL")
    print("1. Operaciones sobre categorías")
    print("2. Operaciones sobre productos")
    print("3. Salir")

def mostrar_menu_operaciones(tabla):
    # Menú de operaciones CRUD para la tabla seleccionada
    print(f"\nOperaciones CRUD para {tabla}")
    print("1. Crear")
    print("2. Leer")
    print("3. Actualizar")
    print("4. Eliminar")
    print("5. Volver al menú principal")

def main():
    while True:
        mostrar_menu_principal()
        opcion_tabla = input("Seleccione una tabla: ")

        if opcion_tabla == "1":  # Operaciones sobre la tabla "categoria"
            while True:
                mostrar_menu_operaciones("categorías")
                opcion_operacion = input("Seleccione una operación: ")

                if opcion_operacion == "1":
                    idcategoria = int(input("Introduzca el ID de la categoría: "))
                    nombre = input("Nombre de la nueva categoría: ")
                    crear_categoria(idcategoria, nombre)
                elif opcion_operacion == "2":
                    leer_categorias()
                elif opcion_operacion == "3":
                    idcategoria = int(input("ID de la categoría a actualizar: "))
                    nuevo_nombre = input("Nuevo nombre de la categoría: ")
                    actualizar_categoria(idcategoria, nuevo_nombre)
                elif opcion_operacion == "4":
                    idcategoria = int(input("ID de la categoría a eliminar: "))
                    eliminar_categoria(idcategoria)
                elif opcion_operacion == "5":
                    break
                else:
                    print("Opción no válida")

        elif opcion_tabla == "2":  # Operaciones sobre la tabla "producto"
            while True:
                mostrar_menu_operaciones("productos")
                opcion_operacion = input("Seleccione una operación: ")

                if opcion_operacion == "1":
                    idproducto = int(input("Introduzca el ID del producto: "))
                    nombre = input("Nombre del nuevo producto: ")
                    idcategoria = int(input("ID de la categoría del producto: "))
                    medida = input("Medida del producto: ")
                    precio = float(input("Precio del producto: "))
                    stock = int(input("Stock del producto: "))
                    crear_producto(idproducto, nombre, idcategoria, medida, precio, stock)
                elif opcion_operacion == "2":
                    leer_productos()
                elif opcion_operacion == "3":
                    idproducto = int(input("ID del producto a actualizar: "))
                    nuevo_nombre = input("Nuevo nombre del producto: ")
                    nueva_categoria = int(input("Nuevo ID de la categoría del producto: "))
                    nueva_medida = input("Nueva medida del producto: ")
                    nuevo_precio = float(input("Nuevo precio del producto: "))
                    nuevo_stock = int(input("Nuevo stock del producto: "))
                    actualizar_producto(idproducto, nuevo_nombre, nueva_categoria, nueva_medida, nuevo_precio, nuevo_stock)
                elif opcion_operacion == "4":
                    idproducto = int(input("ID del producto a eliminar: "))
                    eliminar_producto(idproducto)
                elif opcion_operacion == "5":
                    break
                else:
                    print("Opción no válida")

        elif opcion_tabla == "3":
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida")

main()