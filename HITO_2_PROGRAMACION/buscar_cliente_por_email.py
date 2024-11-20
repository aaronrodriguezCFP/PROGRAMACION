from database import conectar

def buscar_cliente_por_email():
    conexion = conectar()
    if conexion is None:
        return
    
    email = input("Introduce el email del cliente a buscar: ")

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes WHERE email = %s", (email,))
    cliente = cursor.fetchone()

    if cliente:
        print ("cliente encontrado", cliente)
    else:
        print ("cliente no encontrado")

    cursor.close() 
    conexion.close()