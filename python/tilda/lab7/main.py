import timeit,math
from hashfil import Hashtabell
def main():
    h = Hashtabell(2000003)
    filename="unique_tracks.txt"
    with open(filename, "r", encoding="utf-8") as lotFiler:
        for rad in lotFiler:
            temp=rad.strip().split("<SEP>")
            h.put(temp[2],temp)
    # test_name= temp[2]
    # test_name= "Redwan"
    try:
        print(h.get(test_name))
    except KeyError:
        print(test_name," finns inte i hashtabell")
    print(test_name)
main()
