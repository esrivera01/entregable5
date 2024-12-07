# Calculadora interactiva mejorada
def calculadora():
    print("🧮 Calculadora básica:")
    try:
        num1 = float(input("🔢 Introduce el primer número: "))
        num2 = float(input("🔢 Introduce el segundo número: "))
        operacion = input("➕➖✖️➗ Elige una operación (+, -, *, /): ")

        if operacion == "+":
            print(f"✅ Resultado: {num1} + {num2} = {num1 + num2}")
        elif operacion == "-":
            print(f"✅ Resultado: {num1} - {num2} = {num1 - num2}")
        elif operacion == "*":
            print(f"✅ Resultado: {num1} * {num2} = {num1 * num2}")
        elif operacion == "/":
            if num2 != 0:
                print(f"✅ Resultado: {num1} / {num2} = {num1 / num2}")
            else:
                print("❌ Error: División por cero.")
        else:
            print("❌ Operación no válida.")
    except ValueError:
        print("❌ Error: Entrada no válida. Inténtalo de nuevo.")
calculadora()

# Juego de adivinanza con pistas
import random
numero_aleatorio = random.randint(1, 100)
adivinanza = -1

print("🎮 ¡Adivina el número secreto (entre 1 y 100)!")
while adivinanza != numero_aleatorio:
    try:
        adivinanza = int(input("🤔 ¿Cuál crees que es el número? "))
        if adivinanza < numero_aleatorio:
            print("🔼 Pista: El número es mayor...")
        elif adivinanza > numero_aleatorio:
            print("🔽 Pista: El número es menor...")
        else:
            print("🎉 ¡Correcto! Adivinaste el número.")
    except ValueError:
        print("❌ Error: Introduce un número válido.")
