from models.product import Product

class Cart:
    list_items = []

    # Constructor
    def __init__( self ):
        print( self )

    def addProduct( self, product: Product ):
        self.list_items.append( product )
        print( "Product added.." )

    def showProducts( self ):
        print( self.list_items )

    def sumProducts( self ):
        # print( self.list_items )
        total = 0
        for p in self.list_items:
            total += p.price
        return total
