from database import conectar

def crear_pedido(idpedido, idcliente, fechapedido, fechaentrega):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO pedido (idpedido, idcliente, fechapedido, fechaentrega) 
        VALUES (%s, %s, %s, %s)
    """, (idpedido, idcliente, fechapedido, fechaentrega))
    conexion.commit()
    cursor.close()
    conexion.close()
    print(f"Pedido '{idpedido}' creado correctamente.")

def leer_pedidos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT p.idpedido, p.idcliente, p.fechapedido, p.fechaentrega, d.idproducto, d.precio, d.unidades 
        FROM pedido p
        LEFT JOIN detalle d ON p.idpedido = d.idpedido
    """)
    for pedido in cursor:
        print(pedido)
    cursor.close()
    conexion.close()

def actualizar_pedido(idpedido, nuevo_valor):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE pedido SET fechaentrega = %s WHERE idpedido = %s
    """, (nuevo_valor, idpedido))
    conexion.commit()
    cursor.close()
    conexion.close()
    print(f"Pedido '{idpedido}' actualizado correctamente.")

def eliminar_pedido(idpedido):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM pedido WHERE idpedido = %s", (idpedido,))
    conexion.commit()
    cursor.close()
    conexion.close()
    print(f"Pedido '{idpedido}' eliminado correctamente.")

