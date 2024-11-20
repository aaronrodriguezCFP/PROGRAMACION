from database import conectar

def seguimiento_pedido():
    # Conectar a la base de datos
    conexion = conectar()
    if conexion is None:
        return
    
    try:
        # Solicitar el ID del pedido
        pedido_id = input("Introduce el número de pedido: ")
        if not pedido_id.isdigit():
            print("El número de pedido debe ser un valor numérico.")
            return
        
        # Crear cursor
        cursor = conexion.cursor()

        # Consulta de datos del pedido y cliente (corrigiendo 'fecha_pedido' por 'fecha')
        cursor.execute("""
            SELECT p.id, p.fecha, p.total, c.nombre, c.email, c.direccion, c.telefono
            FROM pedidos p
            JOIN clientes c ON p.cliente_id = c.id
            WHERE p.id = %s
        """, (pedido_id,))
        pedido = cursor.fetchone()

        if pedido:
            # Mostrar datos del pedido y cliente
            print("\nDatos del pedido:")
            print(f"Pedido ID: {pedido[0]}")
            print(f"Fecha de pedido: {pedido[1]}")
            print(f"Total: {pedido[2]} €")
            print("\nDatos del cliente:")
            print(f"Nombre: {pedido[3]}")
            print(f"Email: {pedido[4]}")
            print(f"Dirección: {pedido[5]}")
            print(f"Teléfono: {pedido[6]}")

            # Consulta de detalles del pedido
            cursor.execute("""
                SELECT dp.producto_id, dp.cantidad, dp.subtotal, pr.nombre
                FROM detalles_pedido dp
                JOIN productos pr ON dp.producto_id = pr.id
                WHERE dp.pedido_id = %s
            """, (pedido_id,))
            detalles = cursor.fetchall()

            # Mostrar detalles del pedido
            if detalles:
                print("\nDetalles del pedido:")
                for detalle in detalles:
                    print(f"Producto: {detalle[3]}, Cantidad: {detalle[1]}, Subtotal: {detalle[2]} €")
            else:
                print("\nNo se encontraron detalles para este pedido.")
        else:
            print("Pedido no encontrado.")
    
    except Exception as e:
        print(f"Ocurrió un error al procesar el seguimiento del pedido: {e}")
    finally:
        # Cerrar cursor y conexión
        if 'cursor' in locals():
            cursor.close()
        conexion.close()
