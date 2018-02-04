class Node:
    def __init__(self, data, next = None):
        self._data = data
        self._next = next
class LinkedQ:
    def __init__(self):
        self._first = None
        self._last = None
    def __str__(self):
        s=""
        p= self._first
        while p!= None:
            s+= str(p._data)
            p= p.next
        return s.strip()

    def enqueue(self,x):
        nyNode = Node(x)
        if self._last== None:
            self._last = nyNode
            self._first = nyNode
        else:
            self._last._next = nyNode
            self._last = nyNode
    def dequeue(self):
        if self._first==None:
            return None
        else:
            x = self._first._data
            self._next = self._first._next
            if self._next ==None:
                self._first = None
                self._last = None
            else:
                self._first = self._next
            return x
    def isEmpty(self):
        if self._last == None:
            return True
        return False
    def peek(self):
        if not self._first._data:
            raise IndexError("queue is empyt cannot peek")
        return self._first._data
