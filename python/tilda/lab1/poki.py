# first lab !
class PokiGo:

	def __init__(self, name, heal, attack, defence, speed):
		self._name = name
		self._heal = heal
		self._attack = attack
		self._defence = defence
		self._speed = speed

	def __str__(self):
		return self._name + ","+ self._heal + ", " + self._attack+ ", "+ self._defence + ", " + self._speed

	def attack(self):
		return "du har attack värde " + self._attack

	def defence(self):
		print("du har defence värde")
	def speed(self):
		print("du har speed värde")
	def healing(self):
		print("du har healing värde")

	def getName(self):
		return self._name

def soka_namn(lista):
	name = str(input("välj: "))
	for l in lista:
		if l.getName() == name:
			print(l)
		else:
			None


def huvud_meny():
	with open("pokedex.csv", encoding ="utf-8") as fil:
		lista =  []
		for row in fil:
			objekt = row.split(",")
			start = PokiGo(objekt[1],objekt[2],objekt[3],objekt[4],objekt[7])
			lista.append(start)

		print(lista[0].attack())
		start.healing()
		soka_namn(lista)

huvud_meny()
