import sys
from bintreeFile import Bintree
from linkedQFile import LinkedQ
svenska = Bintree()
gamla = Bintree()
q = LinkedQ()
with open("word3.txt", "r", encoding="utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()
        if  ordet in svenska:
            # print(ordet, end=" ")
            continue
        else:
            svenska.put(ordet)
# print("\n")
with open("engelska.txt", "r", encoding="utf-8") as engelskfil:
    for line in engelskfil:
        for i in line.split():
            if i in gamla:
                continue
            else:
                if i in svenska:
                    # print(i,end=" ")
                    pass
                else:
                    gamla.put(i)
# print("\n")
class parentNode:
    def __init__(self,word,parent=None):
        self.word = word
        self.parent = parent
# så länge det finns en parent gör rekursion
# annar printa ut
def writechain(node):
    if node.parent:
        writechain(node.parent)
    print(str(node.word))

def makechildren(node, startOrd, slutOrd):
    temp = list(node.word)
    alphabeter = ['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','å','ä','ö']
    # slinga genom  ord och teken
    for i in range(len(temp)):
        for j in range(len(alphabeter)):
            # byter ordTecken med alfabet
            temp[i] = alphabeter[j]
            # omvanldar från tecken till ord
            nyOrd = "".join(temp)
            # print(nyOrd)
    #         #1 kollar om  nya ordet finns i ordlista men inte i gamla
            if nyOrd in svenska and nyOrd not in gamla:
                gamla.put(nyOrd)
                # vi lägger in node i kön där nyord får attribut word och node som parent
                # det gör att parent pekar på nyord
                q.enqueue(parentNode(nyOrd, node))
            elif nyOrd == slutOrd:
                print("det finns en väg mellan "+ startOrd + " och "+ nyOrd)
                writechain(parentNode(nyOrd, node))
                sys.exit()
        temp = list(node.word)
def main():
    startOrd ="ute"
    slutOrd="hit"
    # skapar en node med attribt word
    nodeOrd=parentNode(startOrd)
    # startOrd ska inte dublicera
    gamla.put(nodeOrd.word)
    # vi lägger in node i kön
    q.enqueue(nodeOrd)
    while q.isEmpty() == False:
        node = q.dequeue()
        makechildren(node, startOrd, slutOrd)
    print("Det finns ingen väg ")
main()
