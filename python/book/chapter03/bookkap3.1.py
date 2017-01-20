# guess my number

# the computer picks a rondom number between 1 to 100
# the player tries to guess it and the computer lets 
# the player know if the guess is too high, too low
# or right on the money 

import random 
print("\t\t\tWelcome to my 'Guess My Number' !")
print("\n\t\tI'm thinking of a number between 1 and 100.")
print("try to guess it in as few attempts as possible.\n")

# set the initial values
the_number= random.randint(1, 100)
guess = int (input("take a guess:"))
tries = 1
# guessing loop
while guess != the_number:
	if guess > the_number:
		print("lower...")
	else:
		print("Higher...")	

	guess = int(input("Take a guess: "))
	tries += 1
print("you guessed it the number was", the_number)
print("and it only took you", tries, "tries!\n")
input("\nPress the enter key to exit.")
