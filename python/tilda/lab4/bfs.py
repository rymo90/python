# lab 4 del 2
# implementation av bredförstsökningen

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

def makechildren(testOrd,q):
    # omvandlar ord till tecken
    temp = list(testOrd)
    alphabeter = ['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','å','ä','ö']
    # lopa genom teken
    for i in range(len(temp)):
        for j in range(len(alphabeter)):
            # byter ordTecken med alfabet
            temp[i] = alphabeter[j]
            # omvanldar från tecken till ord
            nyOrd = "".join(temp)
            #1 kollar om  nya ordet finns i ordlista men inte i gamla
            #2 printer nya order och lägger till i gamla om nya ordet inte lika med startOrd
            if nyOrd in svenska and nyOrd not in gamla:
                if nyOrd == testOrd:
                    continue
                else:
                    q.enqueue(nyOrd)
                    gamla.put(nyOrd)
        temp = list(testOrd)
        # print(temp)

def main():
    startOrd= "söt"
    slutOrd = "sur"
    testOrd = ""
    q.enqueue(startOrd)
    # medan kön är inte tom
    while not q.isEmpty():
        #plockar ut först i kön och gemför med slutOrd
        # om slutOrd finns , slutar programmet skriv meddelande,
        # annars anropa funktion makechildren()
        testOrd= q.dequeue()
        if testOrd == slutOrd:
            print("Det finns en väg till", slutOrd)
            break
        makechildren(testOrd, q)
    # om kön är tom, då har ingen ord hitat
    # skriv ut meddelande
    if testOrd != slutOrd:
        print("Det finns ingen väg till", slutOrd)
main()
