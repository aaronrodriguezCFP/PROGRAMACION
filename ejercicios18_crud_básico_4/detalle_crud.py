from database import conectar

# Crear un nuevo detalle asociado a un pedido
def crear_detalle(idpedido, idproducto, precio, unidades, descuento):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO detalle (idpedido, idproducto, precio, unidades, descuento) 
        VALUES (%s, %s, %s, %s, %s)
    """, (idpedido, idproducto, precio, unidades, descuento))
    conexion.commit()
    cursor.close()
    conexion.close()
    print(f"Detalle para el pedido '{idpedido}' creado correctamente")

# Leer todos los detalles asociados a un pedido
def leer_detalles(idpedido):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM detalle WHERE idpedido = %s", (idpedido,))
    for detalle in cursor:
        print(detalle)
    cursor.close()
    conexion.close()

# Actualizar un detalle de un pedido
def actualizar_detalle(idpedido, idproducto, precio, unidades, descuento):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE detalle SET precio = %s, unidades = %s, descuento = %s 
        WHERE idpedido = %s AND idproducto = %s
    """, (precio, unidades, descuento, idpedido, idproducto))
    conexion.commit()
    cursor.close()
    conexion.close()
    print(f"Detalle del pedido '{idpedido}' actualizado correctamente.")

# Eliminar un detalle de un pedido
def eliminar_detalle(idpedido, idproducto):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM detalle WHERE idpedido = %s AND idproducto = %s", (idpedido, idproducto))
    conexion.commit()
    cursor.close()
    conexion.close()
    print(f"Detalle del pedido '{idpedido}' con producto '{idproducto}' eliminado correctamente.")

