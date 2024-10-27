#Ejercicio 2: Piedra, papel o tijera
import random #importamos esta biblioteca para poder generar un número random

def jugar(): 
    opciones = ["piedra", "papel", "tijera"] #Opciones del juego
    jugador_puntos = 0 #contador de partidas ganadas del jugador
    maquina_puntos = 0 #contador de partidas ganadas por la maquina

    while jugador_puntos < 3 and maquina_puntos < 3: #Mientras ninguno de los 2 gane 3 partidas el juego continuará
        print("***Ejecución iniciada***")
        while True:
            jugador = int(input("Elige 1. Piedra / 2. Papel / 3. Tijera: ")) #Pedimos al jugador que elija una opción
            if jugador in (1, 2, 3): #Si el jugador elige una opción válida
                break 
            else: #Si el jugador elige una opción inválida
                print("Esta opción no existe, prueba otra vez") #Mostramos el mensaje de error

        print(f"El jugador ha elegido {opciones[jugador -1]}") #las listas en python empiezan desde 0 pongo "jugador-1"


        maquina = random.randint(1, 3) #generamos un número aleatorio entre 1 y 3 que son las opciones del juego
        print(f"La maquina ha elegido {opciones[maquina -1]}") 

        if jugador == maquina: #Si el jugador y la máquina eligieron la misma opción
            print("Empate :)") 
        elif (jugador == 1 and maquina == 3) or (jugador == 2 and maquina == 1) or (jugador == 3 and maquina == 2): #Si el jugador ganó a la máquina (poniendo todas los casos en el que el jugador gane)
            print("El jugador ganó la partida:)")
            jugador_puntos += 1 #Se suma 1 al contador de puntos del jugador
        else: #Si la máquina ganó al usuario
            print("La máquina ganó la partida:)")
            maquina_puntos += 1 #Se suma 1 al contador de puntos de la máquina

    #Vamos a mostrar la puntuación del juego
    print(f"El jugador ha ganado {jugador_puntos} - La máquina ha ganado {maquina_puntos}")
    print("***Fin de la partida\n***")

    #Vamos a mostrar quien gana 3 partidas primero
    if jugador_puntos == 3:
        print("El jugador ha ganado 3 partidas, fin del juego")
    else:
        print("la máquina ha ganado 3 partidas, fin del juego")

jugar()  # llamamos a la función