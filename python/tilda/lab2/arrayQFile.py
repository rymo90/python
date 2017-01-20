from array import array

class ArrayQ:# föreläsning 2
    def __init__(self):  # en tom lista
        self._lista = array('l')

    def enqueue (self, nummer):         #  en motod som lägger till i lista
        return self._lista.append(nummer)

    def dequeue (self):    # tar bor och returnera värden
        return self._lista.pop(0)

    def isEmpty (self):          # kollar om lista är tom
        if self._lista == array('l'):
            return True
        else:

            return False
