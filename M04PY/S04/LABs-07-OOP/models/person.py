# 0701 Person Class 
# Crear clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

# Un constructor, donde los datos pueden estar vacíos.

# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.

# mostrar(): Muestra los datos de la persona.

# esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad

class Person:
    
    _name: str
    _age: int
    _rfc: str
    
    hobbie = "Sleeping..."

    def __init__( self, name, age, rfc ):
        self._name = name
        self._age = age
        self._rfc = rfc

    def show( self ):
        return "Mi nombre es " + self.name + ", mi edad es " + str( self.age ) + ", mi rfc es " + self.rfc

    # Creando un getter ( leer el valor de un atributo)
    # Creando un setter ( asignar un valor a un atributo)
    @property
    def name( self ):
        return self._name
    @name.setter
    def name( self, new_name ):
        self._name = new_name

    @property
    def age( self ):
        return self._age

    @property
    def rfc( self ):
        return self._rfc
