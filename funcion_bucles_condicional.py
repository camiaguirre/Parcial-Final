# Ejercicio 4 - Bucles y Condicionales - Adivina el Número

import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    print("¡¡¡Bienvenido al juego!!!")
    intentos = 0

    while True:
        intento = int(input("Ingrese un número: "))
        intentos += 1

        if intento == numero_secreto:
            print(f"¡¡¡Excelente!!! ¡Haz adivinado el número en {intentos} intentos!")
            break
        elif intento < numero_secreto:
            print("Demasiado Bajo...")
        else:
            print("Demasiado Alto...")
            
juego_adivinanza()