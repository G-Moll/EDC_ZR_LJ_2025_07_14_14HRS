# 0703 Account SubClass
# Crear clase llamada Cuenta Joven que deriva de la anterior.

# Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Construye los siguientes métodos para la clase:

# Un constructor.

# Los setters y getters para el nuevo atributo.

# En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad; por lo tanto hay que crear un método es TitularVálido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.

# Además la retirada de dinero sólo se podrá hacer si el titular es válido.

# El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

# Piensa los métodos heredados de la clase madre que hay que reescribir.

# Clases Padre/Superclase/Base
# Clases Hijo/Subclase/Derivada

from models.person import Person
from models.account import Account

class YoungAccount( Account ):

    _accountBonus: float

    def __init__( self, customerData: Person, quantity: float = 0, accountBonus: float = 0  ):

        super().__init__( customerData, quantity )
        self._accountBonus = accountBonus
    
        # if not self.validateCustomer():
        #     print( "Usuario no cumple con la edad requerida" )

    def validateCustomer( self ):
        # if hasattr( self, "_customer") and self._customer:
        if self.customer:
            return self.customer.age >= 18 and self.customer.age < 25
        return False

    @property
    def bonus( self ):
        return self._accountBonus




