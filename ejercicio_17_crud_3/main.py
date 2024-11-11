# main.py
from categoria_crud import crear_categoria, leer_categorias, actualizar_categoria, eliminar_categoria
from producto_crud import crear_producto, leer_productos, actualizar_producto, eliminar_producto
from cliente_crud import crear_cliente, leer_clientes, actualizar_cliente, eliminar_cliente

# Muestra el menú principal para elegir la tabla sobre la que operar
def mostrar_menu_principal():
    print("\nMENÚ PRINCIPAL")
    print("1. Operaciones sobre categorías")
    print("2. Operaciones sobre productos")
    print("3. Operaciones sobre clientes")
    print("4. Salir")

# Muestra el menú de operaciones CRUD para la tabla seleccionada
def mostrar_menu_operaciones(tabla):
    print(f"\nOperaciones CRUD para {tabla}")
    print("1. Crear")
    print("2. Leer")
    print("3. Actualizar")
    print("4. Eliminar")
    print("5. Volver al menú principal")

def main():
    # Diccionarios para seleccionar la función correspondiente según la opción elegida
    operaciones_categoria = {
        "1": lambda: crear_categoria(int(input("ID de la categoría: ")), input("Nombre: ")),
        "2": leer_categorias,
        "3": lambda: actualizar_categoria(int(input("ID: ")), input("Nuevo nombre: ")),
        "4": lambda: eliminar_categoria(int(input("ID: ")))
    }

    operaciones_producto = {
        "1": lambda: crear_producto(
            int(input("ID del producto: ")), input("Nombre: "), int(input("ID categoría: ")),
            input("Medida: "), float(input("Precio: ")), int(input("Stock: "))
        ),
        "2": leer_productos,
        "3": lambda: actualizar_producto(
            int(input("ID: ")), input("Nuevo nombre: "), int(input("Nueva categoría: ")),
            input("Nueva medida: "), float(input("Nuevo precio: ")), int(input("Nuevo stock: "))
        ),
        "4": lambda: eliminar_producto(int(input("ID: ")))
    }

    operaciones_cliente = {
        "1": lambda: crear_cliente(
            input("ID del cliente: "), input("Nombre compañía: "), input("Contacto: "),
            input("Cargo: "), input("Dirección: "), input("Ciudad: "),
            input("Región: "), input("Código postal: "), input("País: "),
            input("Teléfono: "), input("Fax: ")
        ),
        "2": leer_clientes,
        "3": lambda: actualizar_cliente(
            input("ID: "), input("Nuevo nombre compañía: "), input("Nuevo contacto: "),
            input("Nuevo cargo: "), input("Nueva dirección: "), input("Nueva ciudad: "),
            input("Nueva región: "), input("Nuevo código postal: "), input("Nuevo país: "),
            input("Nuevo teléfono: "), input("Nuevo fax: ")
        ),
        "4": lambda: eliminar_cliente(input("ID: "))
    }

    while True:
        mostrar_menu_principal()
        opcion_tabla = input("Seleccione una tabla: ")

        # Submenú para cada tabla
        if opcion_tabla == "1":  # Categorías
            while True:
                mostrar_menu_operaciones("categorías")
                opcion = input("Seleccione una operación: ")
                if opcion == "5": break
                operaciones_categoria.get(opcion, lambda: print("Opción no válida"))()

        elif opcion_tabla == "2":  # Productos
            while True:
                mostrar_menu_operaciones("productos")
                opcion = input("Seleccione una operación: ")
                if opcion == "5": break
                operaciones_producto.get(opcion, lambda: print("Opción no válida"))()

        elif opcion_tabla == "3":  # Clientes
            while True:
                mostrar_menu_operaciones("clientes")
                opcion = input("Seleccione una operación: ")
                if opcion == "5": break
                operaciones_cliente.get(opcion, lambda: print("Opción no válida"))()

        elif opcion_tabla == "4":
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida")

main()
