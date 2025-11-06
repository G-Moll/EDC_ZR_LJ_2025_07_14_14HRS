from models.product import Product
from models.cart import Cart


# DRY Dont Repeat Yourself
product_one = Product( "Leche", 40 )
product_two = Product( "Aceite", 60 )
product_three = Product( "Helado", 100 )
product_four = Product( "Herchy", 35 )
cart = Cart()

cart.addProduct( product_one )
cart.addProduct( product_two )
cart.addProduct( product_three )
cart.addProduct( product_four )
# cart.showProducts()
total_purchase = cart.sumProducts()
print( "Compra total: ", total_purchase )

# print( product_two.name )
# print( product_two.price )


# print( type( product_one ) )
# print( type( product_two ) )
# print( type( cart ) )


