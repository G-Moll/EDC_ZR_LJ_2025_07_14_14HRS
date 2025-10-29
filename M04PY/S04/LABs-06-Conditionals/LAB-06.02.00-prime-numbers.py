import math

def es_primo( numero ):
    """
    Esta función verifica si un número es primo.

    Args:
        numero: El número entero a verificar.

    Returns:
        True si el número es primo, False en caso contrario.
    """
    if numero < 2:
        return False  # Los números menores que 2 no son primos
    
    # Solo es necesario comprobar hasta la raíz cuadrada del número
    for i in range( 2, int( math.sqrt( numero ) ) + 1 ):
        if numero % i == 0:
            return False  # Si es divisible, no es primo
    
    return True  # Si el bucle termina, es primo

# Ejemplo de uso:
numero_a_verificar = 13
if es_primo( numero_a_verificar ):
    print( f"{ numero_a_verificar } es un número primo." )
else:
    print( f"{ numero_a_verificar } no es un número primo." )

numero_a_verificar = 15
if es_primo( numero_a_verificar ):
    print( f"{ numero_a_verificar } es un número primo." )
else:
    print( f"{ numero_a_verificar } no es un número primo." )
