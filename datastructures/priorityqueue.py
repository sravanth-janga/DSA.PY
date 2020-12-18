import sys,os
sys.path.append(os.path.join('.'))
sys.path.append(os.path.join('..'))
from binaryheap import MaxHeap
from Errors.exceptions import Empty

class MaxPriorityQueue(MaxHeap):

    def __init__(self):
        
        super().__init__()

    # inserts element into the priority queue
    def insert(self,val):
        key = float('-inf')
        if isinstance(val,list):
            for v in val:
                self.add(key)
                i = self.heap_size
                self.__increase(i, v) 
        elif isinstance(val, int) or isinstance(val,float):
            self.add(key)
            i = self.heap_size
            self.__increase(i, val)
        else:
            raise Empty('Unsupported type {}. \n only list, int, and float types are supported!'.format(type(val)))

    def __increase(self,i,key):
        if self.list[i]>key:
            raise Empty('Key value should only be increased!')
        self.list[i]=key
        
        while(i>1 and self.list[i]>self.list[self.parent(i)]):
            self.swap(i,self.parent(i))
            i = self.parent(i)
    
    def getmax(self):
        return self.list[1]
        
    def extract_max(self):
        if self.heap_size==0:
            raise Empty('Heap is Empty!')
        val = self.list[1]
        self.nxt = self.heap_size
        self.swap(1,self.heap_size)
        self.heap_size -=1
        self.Max_Heapify(1)
        return val




"""
# driver code
m = MaxPriorityQueue()
m.insert([1,2,2,3,4,3])
print(m.getmax()) """