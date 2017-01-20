# Trust Fund Buddy - Bad
# demonstrates a logical error

print(
"""
			Trust Fund Buddy

Totals you monthly spending so that your trust fund doesn't run out
(and you're forced to get a real job).

Please enter the requested, monthly costs. Since you're rich, ignore Pennies 
and use only dollar amounts.

"""
)

car = input("Lamborghini Tune-ups: ")
rent = input("Manhattan Apartment: ")
jet = input("Private Jet Rental: ")
gifts = input("gifts: ")
food = input("dining out: ")
staff = input("Staff (butlers, chef, driver, assistant): ")
guru = input("Personal Guru and Coach: ")
games = input("Computer Games: ")
total = ( car + rent + jet + gifts + food + staff + guru + games)

print("\nGrand Total:", total)

input("\n\nPress the enter key to exit.")
