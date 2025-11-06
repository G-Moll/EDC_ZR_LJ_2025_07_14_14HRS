# 0803 Fruit Prices
# Programa donde se declare un diccionario para guardar los precios de las distintas frutas. El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

# Diccionario guarde precios de frutas
# Pedirá nombre de la fruta y la cantidad: input
# Mostrará el precio final de la fruta a partir del precio: compra
# Si la fruta no existe mostrar error: mensaje de error
# Tras cada consulta el programa preguntará si queremos hacer otra consulta.

fruits_data =  {}
fruits_data.update( { "avocado": 200 } )
fruits_data.update( { "apple": 40 } )
fruits_data.update( { "bana": 20 } )
fruits_data.update( { "blueberry": 30 } )
fruits_data.update( { "cherry": 50 } )
fruits_data.update( { "kiwi": 40 } )
fruits_data.update( { "mango": 25 } )
fruits_data.update( { "melon": 20 } )
fruits_data.update( { "orange": 20 } )
fruits_data.update( { "strawberry": 30 } )
fruits_data.update( { "tangerine": 25 } )
fruits_data.update( { "watermelon": 25 } )

while True:
    fruit_choice = input( "Qué quiere comprar: " ).lower()
    fruit_quantity = float( input( "Cuánto va a comprar: " ) )

    if fruit_choice not in fruits_data:
        print( "La fruta que buscas ya se la comieron..." )
    else:
        fruit_price = fruits_data.get( fruit_choice )
        fruit_total = fruit_price * fruit_quantity
        print( "Venta de ", fruit_choice  )
        print( "Total: ", fruit_total )


    new_request_message = """
    ¿Quiere hacer una compra adicional?
    0) Para terminar
    1) Para una nueva compra
    """
    new_request = int( input( new_request_message ) )
    if new_request == 0:
        print( "Gracias por tu compra" )
        break
    elif new_request == 1:
        continue




# print( fruits_data )
