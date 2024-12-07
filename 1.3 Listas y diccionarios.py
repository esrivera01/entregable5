# Lista de estudiantes con formato personalizado
estudiantes = ["Juan", "Ana", "Luis"]
print("🎓 Lista de estudiantes:")
for estudiante in estudiantes:
    print(f"📘 Estudiante: {estudiante}")

# Diccionario de información de contacto
contactos = {
    "Juan": "juan@example.com",
    "Ana": "ana@example.com"
}
print("📇 Información de contacto:")
for nombre, correo in contactos.items():
    print(f"📝 Nombre: {nombre}, ✉️ Correo: {correo}")

# Script para agregar elementos a la lista y actualizar el diccionario
nuevo_estudiante = input("✍️ Introduce el nombre de un nuevo estudiante: ")
estudiantes.append(nuevo_estudiante)
print(f"✅ Lista actualizada de estudiantes: {estudiantes}")

nuevo_contacto = input("📋 Introduce el nombre para actualizar/agregar un contacto: ")
nuevo_correo = input("✉️ Introduce el correo de este contacto: ")
contactos[nuevo_contacto] = nuevo_correo
print(f"✅ Contactos actualizados: {contactos}")
