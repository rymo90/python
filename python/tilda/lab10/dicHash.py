import timeit
class DictHash:
    def __init__(self):
        self.dictionary = {}
    def __getitem__(self,nyckel):
         return self.dictionary[nyckel]
    def __contains__(self,nyckel):
        if self.dictionary[nyckel]== None:
            return False
        else:
            return True
    def store(self,nyckel,data):
        self.dictionary[nyckel] = data
def main():
    # filename = "fil.txt"
    filename  ="unique_tracks.txt"
    dic= DictHash()
    with open(filename, "r", encoding="utf-8") as lotFiler:
        for rad in lotFiler:
            temp=rad.strip().split("<SEP>")
            dic.store(temp[2],temp)
    artist = "Der Mystic"
    dictionary=dic[artist]
    dictid = timeit.timeit(stmt=lambda:dictionary,number=10000)
    print("dictionarysokning tog", round(dictid,4),"sekunder")
main()
