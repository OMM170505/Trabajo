import random

print("¡Bienvenido al juego de adivinar el número!")
numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = input("Adivina un número entre 1 y 100: ")
    intentos += 1
    try:
        intento = int(intento)
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    if intento < numero_secreto:
        print("Demasiado bajo.")
    elif intento > numero_secreto:
        print("Demasiado alto.")
    else:
        print(f"¡Correcto! El número era {numero_secreto}. Lo lograste en {intentos} intentos.")
        break
