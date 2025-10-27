# 0501 Positive Negative
# Programa que imprima si el número es positivo o negativo.

input_value = float( input( "Captura un número: " ) )

if input_value > 0:
    print( "El número es positivo..." )
elif input_value < 0:
    print( "El número es negativo..." )
elif input_value == 0:
    print( "El número es neutro..." )

