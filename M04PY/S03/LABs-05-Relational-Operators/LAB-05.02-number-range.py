# 0502 Number Range
# Programa que imprima si el número ingresado esta en el rango de 1 a 7.

input_value = float( input( "Captura un valor: " ) )

if input_value >= 1 and input_value <= 7:
    print( "El valor está dentro del rango...", input_value )
else:
    print( "El valor NO está dentro del rango...", input_value )

# 1 == 1  True
# 1 != 1  False
