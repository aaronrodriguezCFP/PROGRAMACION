import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="usuario",
    password="contraseña",
    database="ANIMALES"
)

cursor = conexion.cursor()

# Definir el ID del animal a eliminar
animal_id = 10

# Consulta SQL para eliminar el animal
consulta = "DELETE FROM ANIMAL WHERE idAnimal = %s"
cursor.execute(consulta, (animal_id,))

# Confirmar los cambios en la base de datos
conexion.commit()
print("Animal eliminado correctamente")

cursor.close()
conexion.close()
