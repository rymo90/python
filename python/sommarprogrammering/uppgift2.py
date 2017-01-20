# programmeringsteknik webbkurs KTH inlämningsuppgift 2.
# Redwan yassi mohammedberhan
# 10 / 12 / 2015
# jag ska mata in fyra rad med meningar och programmet kommer att sedan att skriva ut
# meningar uppdelad på ett vis sätt. Testen kommer att liknna rondelet, en fransk diktform.

# här skriver ut bara information, vad koden ska göra.
def visa_information():
	print("""\n\n\t DIKTATOMATEN
Skriv in fyra meningar och få ut en rondelet !\n""")
# här skriver vi in mäningar och lägger den i en lista ( i min lista som jag kallade MENNING)
# Detta MENNING är en konstant
def indata_meningar():
	i = 1
	while i < 5:
		mening = input("Skriv din mening nr %s: "  %i )
		i += 1
		MENINGAR.append(mening)
	print("\n")
# detta är min viktigaste funktioner. men hjälp av den kommer jag munipilera mening som jag har matta in i den föregående funktion.
def forsta_stora_ord():
	dela = MENINGAR[0].split()	# den tar första index i MENINGAR och den " splitrar", så att den blir en lista med en skilda ord.
	fyra_forsta = dela[0:4]     # här tar vi den första fyra ord i listan
	ihop_ord= " ".join(fyra_forsta) # här har vi nu en sträng !
	return ihop_ord

def rest_forsta_mening():
	dela = MENINGAR[0].split()   # här gör den precis som det föregående funktion.
	rest_mening= dela[4:]		 # men i stället den skriver ut från fiarde till resten av mening
	ihop_ord = " ".join(rest_mening)
	print(ihop_ord)

def rest_andra_meningar(andra, tredje, fjarde):
	print(andra)						# här gör den ingen ändring bara printar ut den inmatade mening.
	print(tredje)
	print(fjarde)

def huvud_functionen():					# här skriver den ut information display
	visa_information()
	indata_meningar()
	dem = forsta_stora_ord()			# här skapar vi en object.
	print(dem.upper(), end = " ")		# och den skriver ut det rutur värde som vi fick och gör den till stor bokstav.
	print("\n")							# här gör de rad bryttning
	kid = forsta_stora_ord()
	print(kid)							# här skapar vi en object. som vi kommer att använda den flera gånger.
	rest_forsta_mening()
	print(kid)
	rest_andra_meningar(MENINGAR[1], MENINGAR[2], MENINGAR[3])
	print(kid)

MENINGAR = []							# här har vi en konstanten. MENNING. som lagrar alla mina inmatningar meningar.
huvud_functionen()						# här har vi huvud programmet. som kommer att anropas till funktionkropp def huvud_funktion. man kan tänkta sig att programmet börajar här.
input("press the enter key to exit.")
