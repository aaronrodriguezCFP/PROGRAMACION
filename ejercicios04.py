#Ejercicios de programación en Python
#EJ1: Contar números pares
#creamos la función
def contar_pares(numeros):
    contador = 0 #inicializamos contador
    for numero in numeros:
        if numero % 2 == 0: #Verificamos si el número es par (si el resto de dividirlo por 2 es 0).

            contador += 1 # SE SUMA UNO
    return contador
# Ejemplo de uso
print(contar_pares([1, 2, 3, 4, 5, 6]))


#EJ2: Encontrar el máximo en una lista
#creamos la función
def encontrar_maximo(numeros):
    if len(numeros) == 0: # Verificar si la lista está vacía
        return None # Si está vacía, devolvemos None
    maximo = numeros[0]

    for numero in numeros: #Recorremos la lista
        if numero > maximo: #Si encontramos un número mayor, se actualiza el máximo
            maximo = numero
    return maximo #Devolvemos el número más grande
    print(encontrar_maximo([3, 5, 2, 9, 1]))

    