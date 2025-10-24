# 0203 Área de un Rectángulo
# Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = float( input( "Captura la base: " ) )
height = float( input( "Captura la altura: " ) )

perimeter = ( base + height ) * 2
area = base * height

print( "El perímetro es: ", perimeter )
print( "El área es: ", area )
