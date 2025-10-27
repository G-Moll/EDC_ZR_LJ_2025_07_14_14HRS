# 0503 Quantity Interest
# Programa que calcule el interés de una cantidad si es mayor al 30%, si no informa el importe total.

# $ 100   % 30
# $ 100   % 30.000001
# $ 100   % 31
# $ 200   % 25
# $ 200   % 50

quantity = float( input( "Capture una cantidad: " ) )       # 200
interest = float( input( "Capture el interés: " ) ) / 100   # 35 -> 0.35 
total = 0

if interest > 0.3:
    total = quantity + ( quantity * interest )
    print( "El total es: ", total )
else:
    print( "El total es: ", quantity )


