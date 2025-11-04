# 0902 Square Numbers
# Obtener el cuadrado de todos los elementos en la lista.

# Lista: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 25, 14, 21

def squareNumbers( list_numbers ):
    squared_numbers = []
    
    for n in list_numbers:
        squared_numbers.append( n * n )

    return squared_numbers

list_values = [ 3, 4, 5, 6, 7, 8 ]
list_squared = squareNumbers( list_values )

print( "Lista original: ", list_values )
print( "Lista de cuadrados: ", list_squared )
