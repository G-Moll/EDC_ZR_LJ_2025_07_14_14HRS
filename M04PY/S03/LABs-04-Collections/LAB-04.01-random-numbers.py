# 0401 Random Numbers
# Programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

import random

list_numbers = []

for i in range( 1, 11 ): # 1 2 3 .... 10
    random_number = random.randint( 1, 10 )
    list_numbers.append( random_number )
    print( "Número: ", random_number )
    print( "\tCuadrado: ", random_number * random_number )
    print( "\tCubo: ", random_number * random_number * random_number )
print( "Todos los números: ", list_numbers )
