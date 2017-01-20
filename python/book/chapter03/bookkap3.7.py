# losing battle 
# avoids the dreaded infinite loop

print("your lone hero is surrounded by a massive army of trolls.")
print("their decaying green bodies stretch out melting into the horizon.")
print("your hero unsheathes his word for the last fight of his life.\n")

health = 10
trolls = 0
damage = 3

while health > 0:
	trolls += 1
	health -= damage

	print("your hero swings and defeats an evil troll, " \
		  "but takes", damage, "damage points.\n"

print("your hero fought valiantly and defeated", trolls, "trolls.")
print("but alas, your hero is no more.")

input("\n\n press the enter key to exit.")
		  