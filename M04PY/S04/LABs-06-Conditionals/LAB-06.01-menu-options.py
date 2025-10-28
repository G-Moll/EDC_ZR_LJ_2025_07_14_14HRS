# 0601 Menu Options
# Menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”.
# Menú, donde podemos escoger las distintas opciones
# hasta que seleccionamos la opción de “Salir”.

print( """
Selecciones las opciones que necesite:
    1) Café             4) Huevos revueltos  7) Pan de dulce
    2) Leche            5) Chilaquiles       8) Hot Cakes
    3) Jugo de naranja  6) Sandwich          9) Postre

    0) Salir
""" )

menu_options = [ "Café", "Leche", "Jugo de naranja", "Huevos revueltos", "Chilaquiles", "Sandwich", "Pan de dulce", "Hot Cakes", "Postre" ]
choices = []

while True:
    input_choice = int( input( "Selecciona alguna opción: " ) )

    if input_choice == 0:
        break
    elif input_choice >= 1 and input_choice <= len( menu_options ):
        choices.append( menu_options[ input_choice - 1 ] )
    # elif input_choice == 1:
    #     choices.append( menu_options[ input_choice - 1 ] )
    # elif input_choice == 2:
    #     choices.append( menu_options[ input_choice - 1 ] )
    # elif input_choice == 3:
    #     choices.append( menu_options[ input_choice - 1 ] )
    # elif input_choice == 4:
    #     choices.append( menu_options[ input_choice - 1 ] )
    # elif input_choice == 5:
    #     choices.append( menu_options[ input_choice - 1 ] )
    # elif input_choice == 6:
    #     choices.append( menu_options[ input_choice - 1 ] )
    # elif input_choice == 7:
    #     choices.append( menu_options[ input_choice - 1 ] )
    # elif input_choice == 2:
    #     choices.append( menu_options[ input_choice - 1 ] )
    # elif input_choice == 8:
    #     choices.append( menu_options[ input_choice - 1 ] )
    # elif input_choice == 9:
    #     choices.append( menu_options[ input_choice - 1 ] )


print( choices )
