#input
x = (1-30)
import random

#processing
def adivinar_numero(x):
    numero_secreto = random.randint(1, 30)
    intentos = 0

    print("Intenta adivinar un número entre 1 y 30.")

    while True:
        intento = int(input("¿Cuál es tu número?: "))
        intentos += 1

        if intento == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
        elif intento < numero_secreto:
            print("fallaste el numero correcto es mayor. ¡Intenta de nuevo!")
        else:
            print("fallaste el numero correcto es menor. ¡Intenta de nuevo!")

#output
# Llamamos a la función para iniciar el juego
adivinar_numero(x)
