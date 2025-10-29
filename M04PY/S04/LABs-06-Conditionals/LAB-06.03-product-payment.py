# 0603 Product Payment
# Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Determinar el pago  mensual  y el total pagado durante los 20 meses.

# Pagar en 20 meses
# El primer mes pagó 10 €
# El segundo 20 €
# El tercero 40 €
# y así sucesivamente

# Determinar el pago  mensual: 10, 20, 40, 80, 160, 320, 720, 1440...
# y el total pagado durante los 20 meses.
                        # 1     2   3   4   5
base_payment = 10       # 10    10
current_payment = 0     # 10    20  40  80  160
total_payment = 0       # 10    30  70  150 310

for m in range( 1, 21 ):
    if m == 1:
        current_payment = base_payment
    else:
        # current_payment = current_payment * 2
        current_payment *= 2
    # total_payment += total_payment + current_payment
    total_payment += current_payment
    print( "Pago mes", m, current_payment )
print( "Pago del coppel", total_payment )
