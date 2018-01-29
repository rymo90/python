import math, timeit,sys
class sokningsorting:
    def __init__(self,track=None,lot=None,artist=None,titel=None):
        self.track= track
        self.lot = lot
        self.artist = artist
        self.titel = titel
    def __lt__(self,other):
        return self.artist < self.artist
    def __repr__(self):
        return "%s " % (self.artist)
    def readfile(self,filename):
        lista= []
        dic ={}
        with open(filename, "r", encoding="utf-8") as lotFiler:
            for rad in lotFiler:
                temp=rad.strip().split("<SEP>")
                obj= sokningsorting(temp[0],temp[1],temp[2],temp[3])
                lista.append(obj)
                dic[obj.artist] = obj
        return lista, dic
    def linearSearch(self, lista,testArtist):
        for i in range(len(lista)):
            if testArtist == lista[i]:
                print(testArtist)
    def mergeSort(self,lista):
        if len(lista) > 1:
            mid=len(lista)//2
            leftHalf=self.mergeSort(lista[:mid])
            rightHalf=self.mergeSort(lista[mid:])
            j=0
            i=0
            k=0
            while i<len(leftHalf)and j< len(rightHalf):
                if leftHalf[i].artist< rightHalf[j].artist:
                    lista[k]=leftHalf[i]
                    i+=1
                else:
                    lista[k]=rightHalf[j]
                    j+=1
                k+=1
            while i<len(leftHalf):
                lista[k]=leftHalf[i]
                i+=1
                k+=1
            while j<len(rightHalf):
                lista[k]=rightHalf[j]
                j+=1
                k+=1
        return lista
    def binSokning(self,Array, target):
        result = 1
        mina = 0
        maxa = len(Array)-1
        while mina <= maxa:
            guess = (mina+maxa)//2
            if Array[guess].artist < target:
                mina = guess+ 1
            elif Array[guess].artist > target:
                maxa = guess -1
            else:
                return Array[guess].artist
            result+=1
        return result
def main():
    s = sokningsorting()
    # filename  ="unique_tracks.txt"
    filename = "fil.txt"
    lista, dic =s.readfile(filename)
    n = len(lista)
    sista = lista[n-1]
    testArtist = sista.artist
    sorterad= s.mergeSort(lista)
    linjTid = timeit.timeit(stmt=lambda:s.linearSearch(lista,testArtist),number=10000)
    print("linjärsökningen tog", round(linjTid,4),"sekunder")
    sortingTid = timeit.timeit(stmt=lambda:s.mergeSort(lista),number=10000)
    print("sorteradtid tog", round(sortingTid,4),"sekunder")
    binsTid = timeit.timeit(stmt=lambda:s.binSokning(sorterad, testArtist)
,number=10000)
    print("Binsokningtid tog", round(binsTid,4),"sekunder")
    dictionaryTid = timeit.timeit(stmt=lambda:dic[testArtist],number=10000)
    print("dictionarytid tog", round(dictionaryTid,4),"sekunder")
main()
## kommenar
# 1)  linjtid(rad.55) for x i
