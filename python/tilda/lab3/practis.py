class Node:
    def __init__(self, data):
        self.leftChild = None
        self.rightChild = None
        self.data = data

    def insert_till(self, value):
        if self.data == value:
            return False
        elif self.data > value:
            if self.leftChild:
                return self.leftChild.insert_till(value)
            else:
                self.leftChild = Node(value)
                return True
        else:
            if self.rightChild != None:
                return self.rightChild.insert_till(value)
            else:
                self.rightChild = Node(value)
                return True

    def find_till(self, value):
        if self.data == value:
            return True
        elif self.data > value:
            if self.leftChild != None:
                return self.leftChild.find_till(value)
            else:
                return False
        else:
            if self.rightChild != None:
                return self.rightChild.find_till(value)
            else:
                return False





class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            return self.root.insert_till(value)
        else:
            self.root = Node(value)
            return True

    def find(self, value):
        if self.root != None:
            return self.root.find_till(value)
        else:
            return False

start = Tree()
start.insert(2)
start.insert(5)
start.insert(6)
start.insert(1)
print(start.find(2))
print(start.find(5))
print(start.find(10))
