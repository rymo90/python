import sys
from bintreeFile import Bintree
from linkedQFile import LinkedQ
svenska = Bintree()
gamla = Bintree()
q = LinkedQ()

def writeChain(node, stepNumber=1): #Recursively writes all the connections from node and upwards.
	if node.parent:
		writeChain(node.parent, stepNumber+1)
	print(str(stepNumber) + ": " + node.value)

def makeChildren(node):
	for n in range(3):
		for char in sweAlpha:
			testWord = list(node.value)
			testWord[n] = char
			testWord = "".join(testWord)

			if testWord == endWord:
				print("En väg hittad mellan " + startWord + " och " + testWord)
				writeChain(ParentNode(testWord,node))
				sys.exit()

			elif svenska.exists(testWord):
				if not gamla.exists(testWord):
					gamla.put(testWord)
					q.put(ParentNode(testWord,node))



sweAlpha = list("abcdefghijklmnopqrstuvwxyzåäö")

with open("texts/word3.txt","r") as wordLines:
	for word in wordLines:
		word = word.rstrip("\n")
		if not svenska.exists(word):
			svenska.put(word)

print("Detta program kommer hitta den snabbaste vägen mellan två trekaraktärs-ord.")
startWord = input("Startord:")
endWord = input("Slutord:")

startNode = ParentNode(startWord)

gamla.put(startNode.value)
q.put(startNode)

while not q.isEmpty():
	node = q.get()
	makeChildren(node)

print("Ingen möjlig väg. Testa igen med nytt slut/startord.")
