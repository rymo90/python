# Losing Battle 
# Demonstrates the dreaded infinite loop

print("you lone here is surrounded by a massive army of trolls.")
print("Their decaying green bodies stretch out, melting into the horizon.")
print("you hero unsheathes his sword for the last fight of this lifel.\n")

health = 10
trolls = 0
damage = 3

while health != 0:
	trolls += 1
	health -= damage

	print("your hero sweings and defeats an evil troll, " \
		   " but takes", damage, "damage points.\n")
print("your hero fought valiantly and defeated", trolls, "trolls.")
print("But alas, your hero is no more. ")

input("\n\nPress the enter key to exit.")

	
