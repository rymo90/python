class Node:
     def __init__(self, value, next = None):
          self._value = value          # värden attribut
          self._next = next            # attribut som pikar på  nästa

class LinkedQ:
     def __init__(self):
        self.first = None
        self.last = None

     def enqueue (self, value):
         ny = Node (value)
         if self.first == None:  
              self.first = ny
              self.last = ny
         else:
              self.last._next = ny
              self.last = ny   # den nya blir sist

     def dequeue (self):
          x = self.first._value
          self.first = self.first._next
          return x

     def isEmpty (self):   # kollar om det är första tom
          if self.first == None:
               return True
          else:
               return False

#array = användbar för memory effectivitiet
#lista  =  snabbare än lista
