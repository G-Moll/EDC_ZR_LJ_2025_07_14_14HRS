# 0201 Convertir de Grados F > C
# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:  ([°F] − 32) × 5 ⁄ 9.

fahrenheit = float( input( "Captura los grados F: " ) )
celcius = ( fahrenheit - 32 ) * 5 / 9
print( "La temperatura es: ", celcius )


