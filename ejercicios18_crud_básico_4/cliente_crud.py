# cliente_crud.py
from database import conectar

# Crear un nuevo cliente
def crear_cliente(idcliente, cia, contacto, cargo, direccion, ciudad, region, cp, pais, tlf, fax):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO cliente (idcliente, cia, contacto, cargo, direccion, ciudad, region, cp, pais, tlf, fax) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (idcliente, cia, contacto, cargo, direccion, ciudad, region, cp, pais, tlf, fax))
    conexion.commit()
    cursor.close()
    conexion.close()
    print(f"Cliente '{cia}' creado correctamente.")

# Leer todos los clientes
def leer_clientes():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM cliente")
    for cliente in cursor:
        print(cliente)  # Muestra cada cliente
    cursor.close()
    conexion.close()

# Actualizar datos de un cliente
def actualizar_cliente(idcliente, cia, contacto, cargo, direccion, ciudad, region, cp, pais, tlf, fax):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE cliente SET cia = %s, contacto = %s, cargo = %s, direccion = %s, ciudad = %s,
        region = %s, cp = %s, pais = %s, tlf = %s, fax = %s WHERE idcliente = %s
    """, (cia, contacto, cargo, direccion, ciudad, region, cp, pais, tlf, fax, idcliente))
    conexion.commit()
    cursor.close()
    conexion.close()
    print(f"Cliente con ID '{idcliente}' actualizado correctamente.")

# Eliminar un cliente por ID
def eliminar_cliente(idcliente):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM cliente WHERE idcliente = %s", (idcliente,))
    conexion.commit()
    cursor.close()
    conexion.close()
    print(f"Cliente con ID '{idcliente}' eliminado correctamente.")
