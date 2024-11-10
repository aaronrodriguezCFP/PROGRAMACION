import mysql.connector

def conectar():
    # Establece la conexión a la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="curso",
        database="supermercado"
    )
    return conexion
