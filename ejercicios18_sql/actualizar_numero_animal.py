import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="usuario",
    password="contraseña",
    database="ANIMALES"
)

cursor = conexion.cursor()

# Definir los nuevos datos
nueva_cantidad = 5
animal_id = 1  # ID del animal a actualizar

# Consulta SQL para actualizar la cantidad
consulta = "UPDATE ANIMAL SET cuantos = %s WHERE idAnimal = %s"
cursor.execute(consulta, (nueva_cantidad, animal_id))

# Confirmar los cambios en la base de datos
conexion.commit()
print("Cantidad actualizada correctamente")

cursor.close()
conexion.close()
