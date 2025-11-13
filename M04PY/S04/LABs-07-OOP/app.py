from models.person import Person
from models.account import Account
from models.youngAccount import YoungAccount

# instancia (de una clase), object
person_one = Person( "Joshua", 30, "JHS3337" )
person_two = Person( "Andrew", 22, "AND2228" )
# account = Account( person_one, 100 )

# account.describe()

young_account_one = YoungAccount( person_one )
# print( "Usuario cumple con los requisitos: ", young_account_one.validateCustomer() )
# young_account_one.describe()
# print( young_account_one.customer.show() )

young_account_two = YoungAccount( person_two )
print( "Usuario cumple con los requisitos: ", young_account_two.validateCustomer() )
# young_account_two.describe()
# print( young_account_two.customer.show() )

# print( f"{ round( 10.002 + 10.015, 1 ) }%" )


# account.describe()
# account.deposit( 500 )
# # account.describe()
# account.withdraw( 10 )
# # account.describe()




