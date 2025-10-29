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
def customSum( numOne, numTwo, numThree ):
    print( numOne + numTwo + numThree )

def customReturnSum( numOne, numTwo, numThree ):
    return numOne + numTwo + numThree

resultNone = customSum( 10, 5 + 5, 20 - 10 )
resultReturn = customReturnSum( 10, 5 + 5, 20 - 10 )
print( resultNone )
print( resultReturn )
