import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="curso",
    database="ANIMALES"
)

cursor = conexion.cursor()

#Definir los datos del nuevo animal
nuevo_animal = (10, 2, 'Tigre', 2) #idanimal, idFamilia, nombre, cantidad

#consulta SQL para insertar un nuevo animal
consulta= "INSERT INTO ANIMAL (idAnimal, idFamilia, animal, cuantos) VALUES (%s, %s, %s, %s)"
cursor.execute(consulta, nuevo_animal)

#Confirmar los cambios en la base de datos 
conexion.commit()
print("Animal insertado correctamente")

cursor.close()
conexion.close()
