from database import conectar

def ver_clientes():
    conexion = conectar()
    if conexion is None:
        return
    
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    print
    for cliente in clientes:
        print(cliente)
    
    cursor.close()
    conexion.close()