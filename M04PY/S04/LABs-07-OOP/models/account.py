# 0702 Account Class
# Crear clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:

# Un constructor, donde los datos pueden estar vacíos.

# Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.

# mostrar(): Muestra los datos de la cuenta.

# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.

# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
from models.person import Person

class Account:

    _customer: Person
    _quantity: float
    _balance: float

    def __init__( self, customer: Person, quantity: float = 0 ):
        self._customer = customer
        self._quantity = quantity
        self._balance = self._quantity

    def describe( self ):
        print( "Balance", self.balance )

    def deposit( self, income: float ):
        self.balance +=  income
        self.describe()

    def withdraw( self, outcome: float ):
        self.balance -= outcome
        self.describe()

    @property
    def balance( self ):
        return self._balance
    @balance.setter
    def balance( self, ammount ):
        self._balance = ammount

    @property
    def customer( self ):
        return self._customer

    @property
    def quantity( self ):
        return self._quantity
