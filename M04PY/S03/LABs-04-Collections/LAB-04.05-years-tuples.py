# 0405 Years Tuples
# Crea una tupla con los meses del año, pide números al usuario, si el número está entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero.

# Crea tupla con meses del años
    # ( "Ene", "Feb".... "Dic" )
# Capturar números entre 1 y la longitud (1-12) máxima de la tupla
# Mostrar contenido de esa posición
    # 1: Ene, 2: Feb ... 12: Dic
#   Si no mostrar mensaje de error: Valores > 12, Valores < 0
# El programa termina cuando el usuario introduce un cero (0).

print( """
Opción A: Captura 0 para Terminar
Opción B: Captura valores entre 1 y 12 para mostrar un mes
 1: Ene       2: Feb       3: Mar
 4: Abr       5: May       6: Jun
 7: Jul       8: Ago       9: Sep
10: Oct      11: Nov      12: Dic
""" )

months = ( "Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic" )

while True:
    user_option = int( input( "Captura un número: " ) )

    if user_option == 0:
        break
    elif user_option < 0 or user_option > len( months ):
        print( "El valor está fuera del rango de valores..." )
    elif user_option >= 1 and user_option <= len( months ):
        # 1 - 1: Ene, 12 - 1: Dic
        print( months[ user_option - 1 ] )


