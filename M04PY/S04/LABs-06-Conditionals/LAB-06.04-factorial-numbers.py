# 0604 Factorial Nombers
# Aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación.
# Por ejemplo 0! = 0=1).
# Por ejemplo 1! = 1=1).
# Por ejemplo 2! = 1x2=2).
# Por ejemplo 3! = 1x2x3=6).
# Por ejemplo 4! = 1x2x3x4=24).
# Por ejemplo 5! = 1x2x3x4x5=120).
# Por ejemplo 6! = 1x2x3x4x5x6=720).
        # 1                      1    1
        # 1                      2    2
        # 2                      3    6
        # 6                      4    24
        # 24                     5    120

factorial_input = int( input( "Captura un entero: " ) )
factorial_result = 0
current_calculation = 1

if factorial_input > 0:
    print( "Calculando factorial" )
    for n in range( 1, factorial_input + 1 ):
        # current_calculation = current_calculation * n
        current_calculation *= n
    print( "Factorial de ", factorial_input, " es", current_calculation )
elif factorial_input == 0:
    print( "El factorial de 0 es: 1" )
