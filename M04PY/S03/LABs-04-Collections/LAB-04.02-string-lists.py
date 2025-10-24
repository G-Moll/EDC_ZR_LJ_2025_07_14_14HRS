# 0402 String Lists
# Crea una lista e inicializarla con 5 cadenas leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos.

# [ "a", "b", "c", "d", "e" ]
# [ "e", "d", "c", "b", "a" ]

user_options =  []
reverse_options =  []

while len( user_options ) < 5:
    user_input = input( "Captura una palabra: " )
    user_options.append( user_input )
    reverse_options.insert( 0, user_input )

print( user_options )
print( reverse_options )
