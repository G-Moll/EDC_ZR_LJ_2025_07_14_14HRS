# 0404 Group Notes
# Programa en Python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listados con las notas de cada alumno.

# El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.

# Guardar nombres alumnos
# Notas que han obtenido
# Cada alumno puede tener distinta cantidad de notas
# Información en diccionario
#   claves: nombres
#   valores: notas

# Pedir número de alumnos a introducir
# Pedir nombre
# Pedir notas hasta introducir número negativo 20, 10, 8, 2, -1, -10
# Mostrará alumnos
# Mostrar la nota media obtenida de cada uno
# Nota: si hay nombres repetidos el programa dará error.

# 4
students_group = {
    # "raquel": [10, 9.9999999, 10],
    # "rodrigo": [9.9999999, 10],
    # "nataly": [ 10, 20 ],
    # "alejandro": [10]
}
students_quantity = int( input( "Alumnos a capturar: " ) )

# name = "raquel"
# students_group[ name ] = []
# name = "rodrigo"
# students_group[ name ] = []
# name = "nataly"
# students_group[ name ] = []
# name = "alejandro"
# students_group[ name ] = []

for student in range( students_quantity ):
    student_name = input( "Nombre del alumno: " )
    students_group[ student_name ] = []

    while True:
        student_note = float( input( "Captura una calificación: " ))
        if student_note >= 0 and student_note <= 10:
            students_group[ student_name ].append( student_note )
        elif student_note < 0:
            break

print( students_group )
