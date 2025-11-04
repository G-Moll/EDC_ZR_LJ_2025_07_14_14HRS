# 0903 Elements Greater than 5
# Obtener la cantidad de elementos mayores a 5 en la tupla.

# tupla = ( 5, 2, 6, 7, 8, 10, 77, 55, 2, 1, 30, 4, 2, 3 )

number_values = ( 5, 2, 6, 7, 8, 10, 77, 55, 2, 1, 30, 4, 2, 3 )
number_edge = 5

def getUpperNumbers( numbersData, numberEdge ):
    filtered_data = []

    for v in numbersData:
        if v > numberEdge:
            filtered_data.append( v )

    return filtered_data

filtered = getUpperNumbers( ( 10,15,5,3,20 ), number_edge )
print( filtered )
filtered = getUpperNumbers( ( 10,15,5,3,20 ), 10 )
print( filtered )
