class parentNode:
    def __init__(self,word,parent=None):
        self.word = word
        self.parent = parent
class LinkedQ:
    def __init__(self):
        self.rear = None
        self.front = None
        self.length = 0
    def enlueue(self, data):
        node = parentNode(data)
        self.length += 1
        if self.rear == None:
            self.rear = node
            self.front = node
        else:
            self.rear.parent = node
            self.rear = node
    def delueue(self):
        if self.front == None:
            return None
        else:
            tarBort= self.front.word
            self.length -= 1
            self.parent = self.front.parent
            if self.parent == None:
                self.front = None
                self.rear= None
            else:
                self.front = self.parent
            return tarBort

    def isEmpty(self):
        if self.rear == None:
            return True
        else:
            return False
    def size(self):
        return self.length

l = LinkedQ()
def makechildren():
    slutOrd = "fivth"
    lista = ["first","second","therd","fourth","fivth",]
    for i in range(len(lista)):
        node = lista[i]
        l.enlueue(node)
        writechain(l,slutOrd)
def writechain(l, slutOrd):
    x =l.delueue()
    if slutOrd == x:
        return slutOrd
    else:
        writechain(l,slutOrd)
def main():
    makechildren()
    # for i in range(l.size()):
    #     print(l.delueue(), end="-->")
    # print("")
    writechain(l,slutOrd)
main()
class demavaf
