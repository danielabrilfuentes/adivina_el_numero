#input
x = (1-30)
import random

#processing
import random

def adivinar_numero(x):
    numero_secreto = random.randint(1, 30)

    print("He pensado en un número entre 1 y 30. Adivina cuál es.")

    intento = int(input("coloca tu numero: "))

    if intento == numero_secreto:
        print("¡Felicidades! Has adivinado el número correctamente.")
    else:
        if intento < numero_secreto:
            print("El número que pensé es mayor que tu repuesta.")
        else:
            print("El número que pensé es menor que tu respuesta.")
        print(f"Lo siento, el número correcto era: {numero_secreto}")

# Llamamos a la función para iniciar el juego
adivinar_numero(x)
