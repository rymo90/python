# lab 4 de 1
# implementation av bredförstsökning
from bintreeFile import Bintree
from linkedQFile import LinkedQ
svenska = Bintree()
gamla = Bintree()
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

def makechildren(startOrd):
    # omvandlar ord till tecken
    temp = list(startOrd)
    alphabeter = ['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','å','ä','ö']
    # slinga genom tecken
    for i in range(len(temp)):
        for j in range(len(alphabeter)):
            # byter ordTecken med alfabet
            temp[i] = alphabeter[j]
            # omvanldar från tecken till ord
            nyOrd = "".join(temp)
            #1 kollar om  nya ordet finns i ordlista men inte i gamla
            #2 printer nya order och lägger till i gamla om nya ordet inte lika med startOrd
            if nyOrd in svenska and nyOrd not in gamla:
                if nyOrd == startOrd:
                    continue
                print(nyOrd)
                gamla.put(nyOrd)
        temp=list(startOrd)
def main():
    startOrd="söt"
    slutOrd="sur"
    makechildren(startOrd)
main()
