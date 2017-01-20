# Exclusive Network
# Demonstrates logical operators and compound conditions

print("\tExclusive computer Network")
print("\t\tMembers only!\n")

security = 0

username = ""
while not username:
 	username = input("username: ")

password = ""
while  not password:
 	password = input("password: ")

if username == "m.dawson" and password == "secret":
 	print("hej, mike")	
 	security = 5
elif username == "s.meier" and password == "civilization":
 	print("hej, sid.")
 	security = 3 
elif username == "s.miyamoto" and password == " mariobros":
 	print("what's up, shigeru?")
 	security = 3
elif username == "w.wright" and password == " thesims":
 	print("how does it, will? ")
 	security = 3 
elif username == "guest" or password == "guest":
 	print("welcome, guest.")
 	security = 1
else:
    print("logg faild. you're not so Exclusive.\n")

input("\n\nPress the enter key to exit. ")
 
