from .linkedlist import LinkedList
class Queue(LinkedList):
    def __init__(self):
        super().__init__('Empty Queue')
    def pop(self):
        if not self.length:
            self._reporterr()
        val = self.head.val
        self.head = self.head.next
        self.length-=1
        return val
    def append(self,val):
        self.addnode(val)


""" # driver code for queue 
q = Queue()
print(str(q))
for i in range(10):
    q.append(i)
for i in range(4):
    q.pop()

q.traverse() """