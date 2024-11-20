import mysql.connector

# Función para realizar la compra
def realizar_compra():
    # Conectar a la base de datos
    conexion = mysql.connector.connect(
        host="localhost",      # Cambiar si la base de datos no está en localhost
        user="root",           # Usuario de la base de datos
        password="curso",           # Contraseña de la base de datos
        database="gestion_pedidos"  # Nombre de la base de datos
    )
    
    if conexion.is_connected():
        print("Conexion exitosa a la base de datos")
    
    # Obtener el ID del cliente
    cliente_id = int(input("Introduce el ID del cliente: "))
    
    # Consultar los productos disponibles en stock
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, precio, stock FROM productos WHERE stock > 0")
    productos = cursor.fetchall()
    
    if len(productos) == 0:
        print("No hay productos disponibles en stock.")
        conexion.close()
        return  # Salir de la función si no hay productos disponibles

    print("Productos disponibles:")
    for producto in productos:
        print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}, Stock: {producto[3]}")
    
    # Crear un nuevo pedido con el cliente seleccionado
    cursor.execute("INSERT INTO pedidos (cliente_id, total) VALUES (%s, %s)", (cliente_id, 0))
    conexion.commit()

    # Obtener el ID del pedido recién creado
    cursor.execute("SELECT LAST_INSERT_ID()")
    pedido_id = cursor.fetchone()[0]
    
    total = 0  # Total de la compra
    
    while True:
        # Seleccionar productos y cantidades para el pedido
        producto_id = input("Introduce el ID del producto (o 'salir' para finalizar): ")
        
        if producto_id.lower() == "salir":
            break
        
        producto_id = int(producto_id)  # Convertir el ID del producto a entero
        cantidad = int(input("Introduce la cantidad: "))
        
        # Consultar el precio y stock del producto seleccionado
        cursor.execute("SELECT precio, stock FROM productos WHERE id = %s", (producto_id,))
        producto = cursor.fetchone()
        
        if producto and producto[1] >= cantidad:  # Verificar si hay suficiente stock
            subtotal = producto[0] * cantidad
            total += subtotal
            # Insertar el detalle del pedido
            cursor.execute("INSERT INTO detalles_pedido (pedido_id, producto_id, cantidad, subtotal) VALUES (%s, %s, %s, %s)",
                           (pedido_id, producto_id, cantidad, subtotal))
            # Actualizar el stock del producto
            cursor.execute("UPDATE productos SET stock = stock - %s WHERE id = %s", (cantidad, producto_id))
            conexion.commit()
        else:
            print("No hay suficiente stock para ese producto o el producto no existe.")
    
    # Actualizar el total del pedido
    cursor.execute("UPDATE pedidos SET total = %s WHERE id = %s", (total, pedido_id))
    conexion.commit()

    print(f"Compra realizada con éxito. Total: {total:.2f}")
    
    # Cerrar la conexión
    conexion.close()