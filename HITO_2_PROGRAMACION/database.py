import mysql.connector

def conectar():
    #Establecer la conexión a la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="curso",
        database="gestion_pedidos"
    )
    print("Conexion exitosa a la base de datos")
    return conexion
