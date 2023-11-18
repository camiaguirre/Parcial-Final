# Ejercicio 4. Condicionales. Clasificacion de notas

def calcular_puntuacion():
    puntuacion = int(input("Ingresa una puntuación (0/100): "))

    if puntuacion >= 90 and puntuacion <= 100:
        print("Su puntuación ", puntuacion, "es A...Sobresaliente...")
    elif puntuacion >= 80 and puntuacion <= 89:
        print("Su puntuación ", puntuacion, "es B...Bueno...")
    elif puntuacion >= 70 and puntuacion <= 79:
        print("Su puntuación ", puntuacion, "es C...Satisfactorio...")
    elif puntuacion >= 60 and puntuacion <= 69:
        print("Su puntuación ", puntuacion, "es D...Necesita Mejorar...")
    elif puntuacion < 60:
        print("Su puntuación ", puntuacion, "es F...Reprobado...")
    elif puntuacion > 100:
        print("El puntaje ingresado es incorrecto!!!")

calcular_puntuacion()