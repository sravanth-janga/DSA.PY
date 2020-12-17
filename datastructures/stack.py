from .linkedlist import LinkedList
from .Node import Node
class Stack(LinkedList):

    def __init__(self):
        super().__init__('Empty Stack!')      


    def append(self,val):
        cur = Node(val)
        cur.next = self.head
        self.head = cur
        self.length +=1
    def pop(self):
        if not self.length:
            self._reporterr()
        cur = self.head.val
        self.head = self.head.next
        self.length -=1
        # returns the value of top most node and pops it from the stack
        return cur 
    def peek(self):
        return self.head.val 
        # return the value of the latest added node.



        
""" # driver code 
s = Stack()
print(str(s))
for i in range(10):
    s.append(i)
s.traverse()
s.pop()
s.pop()
s.traverse() """