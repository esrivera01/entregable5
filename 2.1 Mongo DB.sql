// Conectar y crear la colección 'Estudiantes'
db.Estudiantes.insertMany([
    { "nombre": "Juan", "edad": 50, "ciudad": "Bogotá" },
    { "nombre": "Ana", "edad": 26, "ciudad": "Medellín" },
    { "nombre": "Luis", "edad": 35, "ciudad": "Cali" }
]);

// Consultar todos los documentos de la colección
db.Estudiantes.find();

// Filtrar estudiantes por ciudad
db.Estudiantes.find({ "ciudad": "Medellín" });

// Consultar estudiantes mayores de 30 años
db.Estudiantes.find({ "edad": { $gt: 30 } });
