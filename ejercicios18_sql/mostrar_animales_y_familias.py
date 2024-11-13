import mysql.connector

#conexion a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="curso",
    database = "animales"
)

#Crear cursor
cursor = conexion.cursor()

#Escribir la consulta SQL
consulta = """
SELECT ANIMAL.animal, FAMILIA.familia
FROM ANIMAL
JOIN FAMILIA ON ANIMAL.idFamilia = FAMILIA.idfamilia;
"""

#Ejecutar la consulta
cursor.execute(consulta)

#Obtener y mostrar los resultados
resultados = cursor.fetchall() #Obtiene todos los resultados de la consulta
for animal, familia in resultados:
    print(f"{animal} es de la familia {familia}")

#Cerrar el cursor y la conexion
cursor.close()
conexion.close()

