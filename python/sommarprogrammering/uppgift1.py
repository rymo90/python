# Programmeringsteknik webbkurs KTH inlämningsuppgift 1.
# namn =  Redwan Yassin Mohammedberhan
# datum =  10 / 11 / 2015
# jag kommer ange ett fyrsifrig tal ( talet får ej dock vara samma )
#    och det kommer att beräkna hur många
#      iterationer det krävs innan process kommer till 6174.

i = 0
kaprekar = 6174
mit_tal = int(input("ange ditt tal: ")) # här ska jag ange mitt tal
# här kommer 'condition' och säger att om mi_tal inte är lika med 6174
# gör följande kod
while mit_tal != kaprekar:
    n = str(mit_tal)
    while len(n) < 4: # om mit_tal är mindre än 4 nummer
        n = "0" + n   # lägg till 0 till mit_tal
    large = int("".join(sorted(n, reverse=True))) # sorterar mit_tal från stor till liten
    small = int("".join(sorted(n)))               # sorterar mit_tal från liten till stor.
    mit_tal = large - small
    i += 1
print("Det tog ", i ," innan det blev kaprekar tal", kaprekar) # här skriver den ut hur många gånger det tog innan det blev kaprekar tal.
input("press the enter key to exit:")
