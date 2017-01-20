

from bintreeFile import Bintree
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ")
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")


engelska = Bintree()
with open("engelska.txt", "r", encoding = "utf-8") as engelskafil:
    for rad in engelskafil:
        wordlist = rad.split()   # lägger till i listan

        for oneword in wordlist:
            wordmedteken = oneword.strip(".") # tar bort , . och hoppar till nästa rad
            wordutankomma = wordmedteken.strip(",")
            word = wordutankomma.strip("\"")


            if word not in engelska:   # hoppar över om det inte finns i svensk lista , annars printar det ut.
                engelska.put(word)            # in i sökträdet
                if word in svenska:
                    print(word, end = " ")
print("\n")
