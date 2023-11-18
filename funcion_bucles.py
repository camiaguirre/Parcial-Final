#Ejercicio 4. Bucles. Numeros Pares

def suma_pares():
    num = int(input("Ingrese un número: "))
    suma_pares = 0

    for i in range(1, num + 1):
        if i % 2 == 0:
            suma_pares += i

    print(f"La suma de todos los números pares desde 2 hasta {num} es: {suma_pares}")

suma_pares()







