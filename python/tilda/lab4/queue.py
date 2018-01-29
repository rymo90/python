class Queue:
    def __init__(self):
        self.items= []
    def isEmpty(self):
        if self.items == []:
            return True
        return False
    def enqueue(self, item):
        return self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
