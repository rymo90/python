from array import array

class ArrayQ():

    def __init__(self):
        self._lista = array('l')

    def enqueue(self,value):
        return self._lista.append(value)


    def dequeue(self):
        return self._lista.pop(0)

    def isEmpty(self):
        if self._lista == []:
            return True
        else:
            return False

q = ArrayQ()
tal = input("ange tal").split()
for _ in tal:
    q.enqueue(int(_))
svar = q.isEmpty()
