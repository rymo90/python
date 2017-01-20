# programmeringsteknik webbkurs KTH inlämningsuppgift 3
# Redwan yassin Mohammedberhan
# 10 / 12 / 2015
# I den här programmet har jag skapat tre olika metoder inom klass. varje metod kommer att representera en attrakton.
# och i huvud programmet kommer jag skapa en object som kommer styra den methoden. jag har även skapat attribut som oxå
# tillhör object.
# mina tre attraktoner består av Bergdalsbana, skräckhuset och spelhuset

import random

class Noje_felt(object):						# här skapar jag en klass, Noje_felt . och den printar ut hälsning.
	""" Ett Nöjes fält """
	print("\n\n\t\tVÄLKOMEN TILL NOJE FÄLT",
		   "\n\t\tHÄR HAR VI TRE OLIKA ATTRAKTIONEN")

	def __init__(self, namn, older, lengd, pengar):		# här har vi en constructor. som atomatisk anropas när ett nytt object skapat.
		self.namn  =namn
		self.older =older
		self.lengd = lengd								# här är mina attribut som jag kommer att använda i min programm.
		self.pengar = pengar
		self.skreck = 0
	def bergdal_bana(self):															# här är min första attraktion. Bergdalsbana.
		if self.pengar >= 200:													# den kommmer bara köra om man har mer eller lika med 200 kr.
			if self.older >= 12 and self.lengd >= 1.50:							# här får man bara åka om man är 15 uppåt och är 1.50 cm uppåt.
				print(" HEJ !! och välkomen till Bergdalsbana !!","\n",
					"Det  kostar 200 kr att åka ")
				self.pengar -= 200												# om man uppfyller de tigare krav. då får man åka och det drar pengar 200 kr.
			elif self.older < 12 and self.lengd > 1.50:
				print(" Tyvär det är tolv uppåt som gäller här")
			elif self.older > 12 and self.lengd < 1.50:							# här säger den om du inte uppfyller kraven.
				print( " tyvär grabben du är inte tillräklig lång","\n"
						" för att åka bergdalsbana")
			else:
				print("du kan inte åka Bergdalsbana!, kom tillbaka när du har blivit äldre och längre")
			print("Du har nu ", self.pengar, "kvar på din konto.")						# kollar hur mycket pengar man har kvar på konto.
		else:
			print("Du har ingen pengar kvar på konto.", self.namn, " Hej då !")			# här printar det ut. om man inte uppfyller den första kraven.


	def skrack_huset(self):														# min andra metod. är en skräck hus.
		if self.pengar >= 100:													# min nästa metod kör bara om man har 100 kr eller uppt.
			if self.older < 15:													# om man är mindre än 15 då kommer den att skriva ut förljande.
				print("~~~~~~~~~~~~~~~~~~~NEJJJJJJJJJJJ!!!~~~~~~~~~~~~~~~~")
				print("jag vill inte vara på skrek husset längre")
			else:
				print("~~~~~~~~~~~~~~~~~WHEEEEEEEEE !!~~~~~~~~~~~~")
				print("Det är jätte kul att vara på skrek husset !")
			self.pengar -= 100												# här drar den pengar oavsett hur gammal man är.
			print("du har nu",self.pengar,"kvar på din konto.")
		else:
			print("Du har ingen pengar kvar på konto.", self.namn, " Hej då !")	 # skriver ut om du inte uppfyller den första kraven.

	def spel_huset(self):												# I min sista attraktion.. låter jag spelar ha en chans att få tjäna lite pengar.
		if self.pengar >= 100:									 		# i min spel huset har spelare tre chanser att gissa rätt nummer mellan 1 till 10.
			nummer= random.randint(1,10) 								# om han gissar rätt kommer han att få tjäna 100 kr..
			gissa = int(input("gissa nummer mellan 1 och 10: "))
			forsok = 1
			while gissa != nummer:
				if forsok == 3:													# efter tre gissning slutar spelet och. han betalar 100 kr.
					self.pengar -= 100
					print("Tyvär du har gissat fel, och din tre försök är slut.",
					   "Det rätta nummer var", nummer,
					  	"kom tillbaka igen")									# här berättar jag för spelar vilket nummmer det var.
					print("du har nu", self.pengar,"kvar på din konto")
					break
				elif gissa > nummer:
					print("gissa lägre")
				else:														# dessutom får spelar hjälp då programmet berättar för spelar om han gissa för högt eller lågt.
					print("gissa högre")
				forsok += 1
				gissa = int(input("ange ditt tal:"))

			if gissa == nummer:
				self.pengar += 100											# om han gissar rätt dock. kommer han att blir belönad genom att hans pegar kommer att öka med 100 kr.
				print("du har gissat det rätt", nummer)
				print("det tog dig ", forsok)
				print("grattis du har nu ", self.pengar,"kvar på din konto!")
		else:
			print("Du har ingen pengar kvar på konto.",self.namn,"Hej då !")	#  och som vanligt gäller samma reglar. spelar måsta ha minst 100 innan han får spela spelet. annars kommer inte programmet att köra.

def huvud_programet():
	namn  = input("vad heter du : ")      					# här kommer inmatningen som kommer sen att spara i attributen.
	older = int(input("hur gammal är du : "))
	lengd = float(input("hur lång är du : "))
	pengar = int(input("hur mycket pengar har du: "))
	start = Noje_felt(namn, older, lengd, pengar)
	velj = None
	while velj != "0":										# här kommer spelar att kunna välja mellan olika attraktionen.
		print\
		("""
		Vad god välj en av detta attraktionen

		0 - Avbrytt
		1 - Bergdalsbana
		2 - Skräckhuset
		3 - Spelhuet
		""")


		velj = input("vad god välj : ")
		print()

		if velj == "0":
			print("Hej då ")

		elif velj == "1":
			start.bergdal_bana()

		elif velj == "2":
			start.skrack_huset()

		elif velj == "3":
			start.spel_huset()

		else:
			print("\Tyvär men", velj,"är inte godtycklig val.")

huvud_programet()
input("\nPress the enter key to exit.")
