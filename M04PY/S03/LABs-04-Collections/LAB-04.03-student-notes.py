# 0403 Student Notes
# Programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

# Leer teclado las 5 notas          while < 5
# Notas Entre 0 y 10                1: 20,  2: 12,  3: -10, 4: 8, 5: 10
#           20  >= 0 (True)    y (And)   20  <= 10 (False)      : False
#           -12 >= 0 (False)   y (And)   -12 <= 10 (True)       : False
#           8   >= 0 (True)    y (And)   8   <= 10 (True)       : True
# Mostrar
#   - todas las notas
#   - la nota media
#   - la nota más alta
#   - la menor.
student_notes = []

while len( student_notes ) < 5:
    current_note = float( input( "Captura una calificación: " ) )
    if current_note >= 0 and current_note <= 10:
        student_notes.append( current_note )

print( "CALIFICACIONES" )
print( "Todas las notas: ", student_notes )
print( "Promedio: ", sum( student_notes ) / len( student_notes ) )
print( "Máxima nota: ", max( student_notes ) )
print( "Mínima nota: ", min( student_notes ) )






