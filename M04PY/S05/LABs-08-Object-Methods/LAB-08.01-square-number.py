# 0801 Square Numbers
# Programa que pida un número por teclado y que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.
# input:        5
# squared_values = { 1: 1, 2: 4, 3: 9, 4: 16, 5: 25 }
# input:        3
# { 1: 1, 2: 4, 3: 9 }

squared_values = {}

limit_keys = int( input( "Cuadrados a calcular: " ) )

for n in range( 1, limit_keys + 1 ):
    squared_values.update( { n: n * n  } )

print( squared_values )    

