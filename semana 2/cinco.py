#Repaso sobre estructuras y tipos de datos en Python
#ejemplo de una estructura de datos y directorios
misalumnos=[
    {
        "nombre":"Ismerai",
        "apaterno":"Velasco",
        "amaterno":"Castillo",
        "edad":18
    },
    {
        "nombre":"Yaretzi",
        "apaterno":"Hernández",
        "amaterno":"Patricio",
        "edad":19
    },
    {
        "nombre":"Jesús Manuel",
        "apaterno":"Sánchez",
        "amaterno":"Pereyra",
        "edad":18
    },
    {
        "nombre":"Francisco",
        "apaterno":"Juárez",
        "amaterno":"Avendaño",
        "edad":19
    },
    {
        "nombre":"Jeremy",
        "apaterno":"Hernándezz",
        "amaterno":"Robles",
        "edad":19
    },
    {
        "nombre":"Geovanny",
        "apaterno":"Cuello",
        "amaterno":"Ginez",
        "edad":20
    }
    
]
print("Mostrar todos los datos de mis alumnos",misalumnos)
print("Mostrar todos los datos del primer alumno:", misalumnos[0])
#buscar alumno por nombre
nalumno="Geovanny"
for alumno in misalumnos:
    if alumno["nombre"] == nalumno:
        print("Alumno encontrado:", alumno)
        break
else:
    print("Alumno no encontrado")