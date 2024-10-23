#ejercico1  
edad = int(input("Ingrese su edad: "))
if edad < 5:
    print("entrada gratuita")
elif edad <=12:
    print("5€")
elif edad <=17:
    print("7€")
else: 
    print("10€")


#ejercicio2
nota = int(input("Ingrese su nota: "))
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("F")


#ejercicio3
numero = int(input("Ingrese un numero: "))
match numero:
    case 1:
        print("lunes")
    case 2:
        print("martes")
    case 3:
        print("miercoles")
    case 4:
        print("jueves")
    case 5:
        print("viernes")
    case 6:
        print("sabado")
    case 7:
        print("domingo")
    case _:
        print("número inválido")


#ejercicio4
edad = int(input("Introduce tu edad"))
if edad < 12:
    categoria = "niño"
elif edad <= 17:
    categoria = "adolescente"
elif edad <= 59:
    categoria = "adulto"
elif edad > 59:
    categoria = "anciano"
print(categoria)

idioma = input("Elige tu idioma")
match idioma:
    case "es":
        print("Español")
    case "en":
        print("Inglés")
    case "fr":
        print("Francés")
    case "_":
        print("Idioma no soportado")
