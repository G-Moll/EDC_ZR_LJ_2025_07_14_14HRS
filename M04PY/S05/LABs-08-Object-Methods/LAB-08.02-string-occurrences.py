# 0802 String Occurrences
# Programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.
# "Lorem ipsum... lorem"
# { "L": 1, "o": 2, "r": 2, "e": 2, "m": 3, " ": 1, "i": 1, "p": 1, "s": 1, "u": 1, "l": 1, }

input_string = "Lorem ipsum... lorem"
string_occurences = {}

print( string_occurences.get( "o" ) )

for c in input_string:
    if not string_occurences.get( c ):
        string_occurences.update( { c: 1 } )
    else:
        current_value = string_occurences.get( c )
        string_occurences.update( { c: current_value + 1 } )

print( string_occurences )

