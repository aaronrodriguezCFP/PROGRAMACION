from database import conectar

def crear_producto(idproducto, nombre, idcategoria, medida, precio, stock):
    #Insertar un nuevo producto en la tabla producto
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO producto (idproducto, nombre, idcategoria, medida, precio, stock) VALUES (%s, %s, %s, %s, %s, %s)",
        (idproducto, nombre, idcategoria, medida, precio, stock)
    )
    conexion.commit()
    cursor.close()
    conexion.close()
    print(f"Producto '{nombre}' creado")

def leer_productos():
    # Lee todos los productos de la tabla "producto"
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM producto")
    for idproducto, nombre, idcategoria, medida, precio, stock in cursor:
        print(f"{idproducto} - {nombre} - {idcategoria} - {medida} - {precio} - {stock}")
    cursor.close()
    conexion.close()

def actualizar_producto(idproducto, nuevo_nombre, nueva_categoria, nueva_medida, nuevo_precio, nuevo_stock):
    # Actualiza un producto existente en la tabla "producto"
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE producto SET nombre = %s, idcategoria = %s, medida = %s, precio = %s, stock = %s WHERE idproducto = %s",
        (nuevo_nombre, nueva_categoria, nueva_medida, nuevo_precio, nuevo_stock, idproducto)
    )
    conexion.commit()
    cursor.close()
    conexion.close()
    print(f"Producto con ID {idproducto} actualizado correctamente")

def eliminar_producto(idproducto):
    # Elimina un producto de la tabla "producto"
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM producto WHERE idproducto = %s", (idproducto,))
    conexion.commit()
    cursor.close()
    conexion.close()
    print(f"Producto con ID {idproducto} eliminado")