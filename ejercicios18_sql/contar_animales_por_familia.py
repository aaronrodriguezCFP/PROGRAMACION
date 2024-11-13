import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="curso",
    database="ANIMALES"
)

cursor = conexion.cursor()

# Consulta SQL para contar los animales por familia
consulta = """
SELECT FAMILIA.familia, COUNT(ANIMAL.animal) AS total_animales
FROM ANIMAL
JOIN FAMILIA ON ANIMAL.idFamilia = FAMILIA.idfamilia
GROUP BY FAMILIA.familia;
"""

cursor.execute(consulta)

# Mostrar los resultados
resultados = cursor.fetchall()
for familia, total in resultados:
    print(f"Familia: {familia}, Total de animales: {total}")

cursor.close()
conexion.close()