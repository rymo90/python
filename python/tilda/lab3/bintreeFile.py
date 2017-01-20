class Node:
    def __init__(self, value):
          self.value = value
          self.left = None
          self.right = None
class Bintree:
    def __init__(self):
        self.root = None

    def put(self, newvalue):       # lägger till värde i binaträd
        self.root = putta(self.root, newvalue)

    def __contains__(self,value):
        return finns(self.root,value)

    def write(self):
        skriv(self.root)
        print("\n")


def putta (root, newvalue):
    if (root == None):                  # lägger till om root är tom
        root = Node(newvalue)
    elif (newvalue < root.value):       # om det är mindre lägger det till vänster
        root.left = putta (root.left, newvalue)

    elif (newvalue > root.value):        # lägger till till höger om det är stort tal
        root.right = putta (root.right, newvalue)

    return root


def finns (root, value):
    if root == None:      # kollar om det finns ord i listan
        return False
    if value == root.value:
        return True
    if value < root.value:
        return finns(root.left,value)
    if value > root.value:
        return finns(root.right,value)


def skriv (root):
    if root != None:            #  skriver ut det.
            skriv (root.left)
            print(root.value)
            skriv (root.right)
