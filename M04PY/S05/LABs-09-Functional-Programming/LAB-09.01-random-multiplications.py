# 0901 Random Multiplications
# Programa que pregunte aleatoriamente una multiplicación. El programa debe indicar si la respuesta ha sido correcta o no (en caso que la respuesta sea incorrecta el programa debe indicar cuál es la correcta). El programa preguntará 10 multiplicaciones, y al finalizar mostrará el número de aciertos.

# Preguntar aleatoriamente una multiplicación
# Indicar si la respuesta es correcta o no
#   - En caso que la respuesta sea incorrecta, mostrar la correcta
# Preguntar 10 multiplicaciones
# Al finalizar mostrar aciertos
import random

def calculateMultiplication():
    mult = {}
    mult[ "num_one" ] = random.randint( 1, 10 )                 #  4
    mult[ "num_two" ] = random.randint( 1, 10 )                 #  5
    mult[ "mult_nums" ] = mult[ "num_one" ] * mult[ "num_two" ] # 20
    return mult

def promptUser():
    attempt_results = { "right": 0, "wrong": 0, "matches": [] }

    for a in range( 10 ):
        current_mult = calculateMultiplication()
        num_one = current_mult[ "num_one" ]
        num_two = current_mult[ "num_two" ]
        mult_nums = current_mult[ "mult_nums" ]
        # print( current_mult, num_one, num_two, mult_nums )

        message = "Resultado de multiplicar " + str( num_one ) + " x " + str( num_two ) + ": "
        
        user_answer = int( input( message ) )

        unmatched = user_answer != mult_nums
        if unmatched:
            attempt_results[ "wrong" ] += 1
        else:
            attempt_results[ "right" ] += 1

        attempt_results[ "matches" ].append( { "pc": mult_nums, "user": user_answer, "matched": not unmatched } )

        # print( user_answer, mult_nums == user_answer )

    return attempt_results
    
def showResults( dataResults ):
    dataDisplay = "";
    dataDisplay += "Correctas: " + str( dataResults[ "right" ] ) + "Incorrectas: " + str( dataResults[ "wrong" ] )
    dataDisplay += "\nRespuestas:"
    for m in dataResults[ "matches" ]:
        msg_string: str
        if m[ "matched" ]:
            msg_string = "Sí"
        else:
            msg_string = "No"
        dataDisplay += "\nCorrecta: " + str( m[ "pc" ] ) + ", Usuario: " + str( m[ "user" ] ) + ", Coniciden: " + msg_string

    return dataDisplay

# results = promptUser()
# showResults( results )

print( showResults( promptUser() ) )
