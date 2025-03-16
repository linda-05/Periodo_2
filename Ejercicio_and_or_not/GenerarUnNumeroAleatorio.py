import random

numero_secreto = random.randint(1,10)
intentos = 0
max_intentos = 5

print("¡Adivina el numero secreto entre 1 y 10!")

while intentos < max_intentos:
    intentos = int(input(f" Intento{intentos + 1}/{max_intentos}:"))

    if intentos == numero_secreto:
        print("!Felicidades Adivinastes el numero¡")
        break # Salimos del bucle si el numero es correcto
    elif intentos < numero_secreto:
        print("El numero es mayor. Intenta de nuevo.")
    else: 
        print("El numero es menor.Inenta de nuevo.")
        intentos += 1
else:
    # se ejecuta solo si el bucle while termina sin un break
    print(f"Has agotado los intentos. El numero era {numero_secreto}")
print("Fin del juego.")