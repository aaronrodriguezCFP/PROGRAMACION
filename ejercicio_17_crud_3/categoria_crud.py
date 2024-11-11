# categoria_crud.py
from database import conectar

def crear_categoria(idcategoria, nombre):
    # Inserta una nueva categoría en la tabla "categoria"
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO categoria (idcategoria, categoria) VALUES (%s, %s)", (idcategoria, nombre))
    conexion.commit()  # Confirma los cambios en la base de datos
    cursor.close()
    conexion.close()
    print(f"Categoría '{nombre}' creada correctamente")

def leer_categorias():
    # Lee todas las categorías de la tabla "categoria"
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM categoria")
    for idcategoria, nombre in cursor:
        print(f"{idcategoria} - {nombre}")
    cursor.close()
    conexion.close()

def actualizar_categoria(idcategoria, nuevo_nombre):
    # Actualiza el nombre de una categoría existente en la tabla "categoria"
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("UPDATE categoria SET categoria = %s WHERE idcategoria = %s", (nuevo_nombre, idcategoria))
    conexion.commit()
    cursor.close()
    conexion.close()
    print(f"Categoría con ID {idcategoria} actualizada a '{nuevo_nombre}'")

def eliminar_categoria(idcategoria):
    # Elimina una categoría de la tabla "categoria"
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM categoria WHERE idcategoria = %s", (idcategoria,))
    conexion.commit()
    cursor.close()
    conexion.close()
    print(f"Categoría con ID {idcategoria} eliminada")




