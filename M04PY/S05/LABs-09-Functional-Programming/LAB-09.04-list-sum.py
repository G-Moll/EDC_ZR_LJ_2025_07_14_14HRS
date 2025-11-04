# 0904 List Sum
# Obtener la suma de todos los elementos en la lista.

def customSum( dataList ):
    totalSum = 0

    for n in dataList:
        totalSum += n
    
    return totalSum

print( "El total es: ", customSum( [ 10, 10, 20 ] ))
print( "El total es: ", customSum( [ 0, 1, 2, 80, 800, 12 ] ))
