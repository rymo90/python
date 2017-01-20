class Node:
    def __init__(self, x):
        self.x = x
        self.right = None
        self.left = None
class igen:
    def __init__(self):
        self.root =None
    def getRoot(self):
        return self.root
    def add(self, x):
        if (self.root==None):
            self.root = Node(x)
        else:
            self._add(x, self.root)
    def _add(self, x, node):
        if (x < node.x):
            if (node.left != None):
                self._add(x, node.left)
            else:
                node.left = Node(x)
        else:
            if (node.right != None):
                self._add(x, node.right)
            else:
                node.right = Node(x)
    def find(self,x):
        if (self.root!=None):
            return self._find(x,self.root)
        else:
            return None
    def _find(self, x, node):
        if (x==node.x):
            return node
        elif(x < node.x and node.left != None):
            self._find(x, node.left)
        elif(x > node.x and node.right != None):
            self._find(x, node.right)

borja = igen()
with open("text2.txt", "r", encoding ="utf-8")as familfil:
    for enrad in familfil:
        dela = enrad.strip()
        if dela in borja:
            print(dela, end=" ")
        else:
            borja._add(dela)
print("\n")
