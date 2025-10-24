# 0400 Collections

# List
#                   0           1           2
students_name = [ "Raquel", "Nataly", "Alejandro" ]
print( students_name )
#                       3
students_name.append( "Rodrigo" )
print( students_name )
print( students_name[ 0 ] )
print( students_name[ 3 ] )
print( students_name[ -1 ] )
print( students_name[ -2 ] )
print( students_name[ -3 ] )
print( students_name[ -4 ] )

# Dictionary
jobs = {
    "in-situ": "Designer",
    "remote": "Súper Jaquer"
}

print( jobs[ "in-situ" ] )
print( jobs[ "remote" ] )


# List contains dictionaries
# Students ( {} ) list ( [] )
students_list = [
    { "name": "Raquel", "hobby": "Run" },
    { "name": "Nataly", "hobby": "Reading" },
    { "name": "Alejandro", "hobby": "Music" },
    { "name": "Rodrigo", "hobby": "Learning" }
]
print( students_list )
print( students_list[ -1 ] )
print( students_list[ -1 ][ "hobby" ] )
print( students_list[ -2 ][ "hobby" ] )
print( students_list[ -3 ][ "hobby" ] )
print( students_list[ 0 ][ "hobby" ] )

# Dictionary contains lists
buildings = {
    "parks": [ "Inbursa", "Kidzania", "Kinezis" ],
    "museums": [ "Bellas Artes", "Soumaya", "Antropología" ]
}
