from categoria_crud import crear_categoria, leer_categorias, actualizar_categoria, eliminar_categoria
from producto_crud import crear_producto, leer_productos, actualizar_producto, eliminar_producto
from cliente_crud import crear_cliente, leer_clientes, actualizar_cliente, eliminar_cliente
from pedido_crud import crear_pedido, leer_pedidos, actualizar_pedido, eliminar_pedido
from detalle_crud import crear_detalle, leer_detalles, actualizar_detalle, eliminar_detalle

def mostrar_menu_tablas():
    """Muestra el menú principal para seleccionar la tabla."""
    print("\n--- MENU PRINCIPAL ---")
    print("1. Categoría")
    print("2. Producto")
    print("3. Cliente")
    print("4. Pedido")
    print("5. Salir")

def mostrar_menu_crud(tabla):
    """Muestra el menú CRUD para la tabla seleccionada."""
    print(f"\n--- Operaciones en {tabla} ---")
    print("1. Crear")
    print("2. Leer")
    print("3. Actualizar")
    print("4. Eliminar")
    if tabla == "Pedido":
        print("5. Operar en Detalles de Pedido")  # Solo para la opción Pedido
    print("6. Volver al menú principal")

def main():
    while True:
        mostrar_menu_tablas()
        opcion_tabla = input("Seleccione una tabla: ")

        if opcion_tabla == "1":
            ejecutar_operacion("Categoría", crear_categoria, leer_categorias, actualizar_categoria, eliminar_categoria)
        elif opcion_tabla == "2":
            ejecutar_operacion("Producto", crear_producto, leer_productos, actualizar_producto, eliminar_producto)
        elif opcion_tabla == "3":
            ejecutar_operacion("Cliente", crear_cliente, leer_clientes, actualizar_cliente, eliminar_cliente)
        elif opcion_tabla == "4":
            ejecutar_operacion("Pedido", crear_pedido, leer_pedidos, actualizar_pedido, eliminar_pedido, es_pedido=True)
        elif opcion_tabla == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def ejecutar_operacion(tabla, crear, leer, actualizar, eliminar, es_pedido=False):
    """Muestra el menú CRUD para una tabla y ejecuta la operación seleccionada."""
    while True:
        mostrar_menu_crud(tabla)
        opcion_crud = input(f"Seleccione una operación en {tabla}: ")

        if opcion_crud == "1":
            crear()
        elif opcion_crud == "2":
            leer()
        elif opcion_crud == "3":
            id_item = input(f"Ingrese el ID del {tabla} a actualizar: ")
            nuevo_valor = input(f"Ingrese el nuevo valor del {tabla}: ")
            actualizar(id_item, nuevo_valor)
        elif opcion_crud == "4":
            id_item = input(f"Ingrese el ID del {tabla} a eliminar: ")
            eliminar(id_item)
        elif es_pedido and opcion_crud == "5":
            ejecutar_operacion_detalle()  # Menú CRUD de Detalles
        elif opcion_crud == "6":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def ejecutar_operacion_detalle():
    """Muestra el menú CRUD para Detalles de Pedido y ejecuta la operación seleccionada."""
    while True:
        print("\n--- Operaciones en Detalles de Pedido ---")
        print("1. Crear Detalle")
        print("2. Leer Detalles")
        print("3. Actualizar Detalle")
        print("4. Eliminar Detalle")
        print("5. Volver al menú de Pedidos")
        
        opcion = input("Seleccione una operación en Detalles: ")

        if opcion == "1":
            # Solicitar datos para crear el detalle
            idpedido = int(input("ID del pedido: "))
            idproducto = int(input("ID del producto: "))
            precio = float(input("Precio del producto: "))
            unidades = int(input("Cantidad: "))
            descuento = float(input("Descuento: "))
            # Crear el detalle
            crear_detalle(idpedido, idproducto, precio, unidades, descuento)
        elif opcion == "2":
            # Solicitar el ID del pedido para leer los detalles asociados
            id_pedido = input("Ingrese el ID del pedido para leer los detalles: ")
            leer_detalles(id_pedido)  # Pasar el id_pedido a la función leer_detalles
        elif opcion == "3":
            # Solicitar datos para actualizar un detalle
            id_pedido = input("ID del pedido del detalle a actualizar: ")
            id_producto = input("ID del producto del detalle a actualizar: ")
            nuevo_precio = float(input("Nuevo precio: "))
            nuevas_unidades = int(input("Nuevas unidades: "))
            nuevo_descuento = float(input("Nuevo descuento: "))
            # Actualizar el detalle
            actualizar_detalle(id_pedido, id_producto, nuevo_precio, nuevas_unidades, nuevo_descuento)
        elif opcion == "4":
            # Solicitar datos para eliminar un detalle
            id_pedido = input("ID del pedido del detalle a eliminar: ")
            id_producto = input("ID del producto del detalle a eliminar: ")
            # Eliminar el detalle
            eliminar_detalle(id_pedido, id_producto)
        elif opcion == "5":
            break  # Vuelve al menú de Pedidos
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
