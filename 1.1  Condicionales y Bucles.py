# Verificar si un número es par o impar
numero = int(input("🔢 Introduce un número: "))
if numero % 2 == 0:
    print("✅ El número es par.")
else:
    print("❌ El número es impar.")

# Bucle for: Imprimir cuadrados de números en una lista
numeros = [1, 2, 3, 4, 5]
print("📐 Cuadrados de los números en la lista:")
for n in numeros:
    print(f"🔹 El cuadrado de {n} es {n**2}")

# Bucle while: Solicitar entrada hasta que el usuario introduzca '0'
entrada = ""
while entrada != "0":
    entrada = input("🖊️ Introduce un número (0 para salir): ")
    if entrada != "0":
        print(f"📋 Has introducido: {entrada}")
print("🔚 ¡Programa finalizado!")
