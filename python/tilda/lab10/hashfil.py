import timeit,math
class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
class Hashtabell:
    def __init__(self,size):
        self.size=(size*2)
        self.table= [None]*self.size
    def getKey(self,nyckel):
        x=0
        for i in range(len(nyckel)):
            x+= ord(nyckel[i])*(x+1)
        return (x%self.size)
    def put(self,nyckel,data):
        get_key= self.getKey(nyckel)
        node = Node(nyckel,data)
        if self.table[get_key]==None:
            self.table[get_key]=node
        else:
            if self.table[get_key].key== nyckel:
                self.table[get_key] = node
            else:
                next_table = self.rehash(get_key,self.size)
                while self.table[next_table]!=None and self.table[next_table].key!= nyckel:
                    next_table= self.rehash(next_table,self.size)
                if self.table[next_table]==None:
                    self.table[next_table]=node
    def get(self,nyckel):
        get_key=self.getKey(nyckel)
        ob= None
        stop= False
        found= False
        position = get_key
        while self.table[position]!=None and not found and not stop:
            if self.table[position].key==nyckel:
                found= True
                ob= self.table[position].value
            else:
                position=self.rehash(position,self.size)
                if position==get_key:
                    stop=True
        if ob:
            return ob
        else:
            raise KeyError
    def __getitem__(self,key):
        return self.get(key)
    def __setitem__(self,key,data):
        self.put(key,data)
    def rehash(self,oldhash,size):
        return (oldhash+1)%size
