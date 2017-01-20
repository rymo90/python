class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    def getRoot(self):
        return self.root
    def add(self, value):
        if(self.root==None):
            self.root = Node(value)
        else:
            self._add(value, self.root)
    def _add(self, value, node):
        if (value < node.value):
            if (node.left != None):
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if (node.right != None):
                self._add(value, node.right)
            else:
                node.right = Node(value)
    def find(self, value):
        if(self.root!= None):
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, node):
        if (value == node.value):
            return node
        elif(value < node.value and node.left != None):
            self._find(value, node.left)
        elif (value > node.value and node.right != None):
            self._find(value, node.right)
    def deletTree(self):
        self.root = None

    def printTree(self):
        if (self.root != None):
            self._printTree(self.root)
    def _printTree(self, node):
        if (node != None):
            self._printTree(node.right)
            print(str(node.value)+ '')
            self._printTree(node.right)

tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
print(tree.find(3).value)
print(tree.find(10))

tree.deletTree()
tree.deletTree()
