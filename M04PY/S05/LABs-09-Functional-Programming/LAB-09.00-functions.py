# 0900 Functions
# Bloques de código reutilizables.
# DRY: Dont Repeat Yourself

# Declare Function
def sayHello():
    print( "Gelou" );

# Run, Execute, Call, Invoke, Evaluate, Use Function
# sayHello()
# sayHello()
# sayHello()

# ================================================================================
#               Parameter
def saySomething( message ):
    print( "Hola " + message )


#               Arguments
# saySomething( "compañeros..." )
# saySomething( "no tan compañeros..." )
# saySomething( "no compañeros..." )

# ================================================================================
# return values
def sumResultNone( numOne, numTwo, numThree ):
    print( numOne + numTwo + numThree )

def sumResultReturn( numOne, numTwo, numThree ):
    return numOne + numTwo + numThree

# resultNone = sumResultNone( 10, 5 + 5, 20 - 10 )
# resultReturn = sumResultReturn( 10, 5 + 5, 20 - 10 )
# print( resultNone, type( resultNone ) )
# print( resultReturn, type( resultReturn ) )

# ================================================================================

# Convenciones de nombres
# numOne    camelCase/Lower CamelCase       variables, funciones
# num_one   snake_case                      variables (Python)
# NumOne    Upper CamelCase/PascalCase      Clases, Interfaces
# num-one   kebab-case                      url

# ================================================================================
# Functional Programming
# 1) Deben resolver una tarea concreta
# 2) Pueden recibir (Parameters) valores
# 3) Los datos se procesan dentro de la función
# 4) No tienen dependencias externas
# 5) Deben devolver datos

def sample( dataAge ):
    return str( dataAge ) + "!!!"

# age = 30

print( sample( 10 ) )
