from database import conectar

def registrar_cliente():
    conexion = conectar()
    if conexion is None:
        return
    
    nombre = input("Introduce el nombre del cliente: ")
    direccion = input("Introduce la direccion del cliente: ")
    email = input("Introduce el email del cliente: ")
    telefono = input("Introduce el telefono del cliente: ")

    cursor = conexion.cursor()
    cursor.execute("INSERT INTO clientes (nombre, direccion, email, telefono) VALUES (%s, %s, %s, %s)",
                   (nombre, direccion, email, telefono))
    conexion.commit()
    print("Cliente registrado correctamente")
    cursor.close()
    conexion.close()

                    