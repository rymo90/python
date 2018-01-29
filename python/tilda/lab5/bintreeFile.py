class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    def putta(self, newValue):
        if self.data== newValue:
            return newValue
        elif self.data > newValue:
            if self.left:
                return self.left.putta(newValue)
            else:
                self.left = Node(newValue)
                return False
        else:
            if self.right:
                return self.right.putta(newValue)
            else:
                self.right = Node(newValue)
                return False
    def finns(self, value):
        if self.data == value:
            return True
        elif self.data > value:
            if self.left:
                return self.left.finns(value)
            else:
                return False
        else:
            if self.right:
                return self.right.finns(value)
            else:
                return False
    # skriver ut inording !!
    def skriv(self):
        if self:
            if self.left:
                self.left.skriv()
            print(str(self.data))
            if self.right:
                self.right.skriv()
class Bintree:
    def __init__(self):
        self.root = None
    def put(self, newValue):
        if self.root:
            return self.root.putta(newValue)
        else:
            self.root = Node(newValue)
            return False
    def __contains__(self,value):
        if self.root:
            return self.root.finns(value)
        else:
            return False

    def write(self):
        if self.root is not None:
            print("skriver ut trädet i inordning")
            return self.root.skriv()
