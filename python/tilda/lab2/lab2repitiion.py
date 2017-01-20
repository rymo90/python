from array import array

class ArrayQ:

    def __init__(self):
        self._data = array('l')

    def dequeu(self):
        return self._data.pop(0)

    def enqueu(self, data):
        return self._data.append(data)

    def isEmpty(self):
        if self._data == array('l'):
            return True
        return False


ob = ArrayQ()
ob.enqueu(3)
ob.enqueu(5)
ob.enqueu(7)
ob.enqueu(9)

print(ob.dequeu())
print(ob.dequeu())
print(ob.dequeu())
print(ob.dequeu())
print(ob.isEmpty())

with open("maud.txt",) as register:
    for rad in register:
        lista = rad.split()
        print(lista[0])
        print(rad[0])
