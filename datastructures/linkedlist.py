from .Node import Node
from Errors.exceptions import Empty
class LinkedList():
    def __init__(self,msg =  'Linked List is Empty'):
        self.head = None
        self.tail = None
        self.msg = msg
        self.length = 0
        self.__str__()
    # my dets
    def __str__(self):
        print( """       
        
            #####################################################################
            #                                                                   #
            # author   : Sravanth Janga,                                        #              
            # github   : https://github.com/sravanth-janga,                     #
            # linkedin : https://www.linkedin.com/in/sravanth-reddy-22771816a/  #
            #                                                                   #
            # ###################################################################

            
        """)
    # add node to the list

    def addnode(self,val):
        node = Node(val)
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = self.head
        self.length +=1
    
    # returns the total number of nodes.
    def __len__(self):
        return self.length

    def _reporterr(self):
        raise Empty(self.msg)
    # traverse
    def traverse(self):
        cur = self.head
        while(cur):
            if(cur.next):
                print(cur.val,'--> ',end='')
            else:
                print(cur.val)
                print('')
            cur = cur.next
        del cur
    
    # delete node
    def delete(self,val):
        if self.length==0:
            self._reporterr()
        f = True
        cur = self.head
        prev = None
        while(cur):
            if cur.val == val:
                break
            prev = cur
            cur = cur.next
        if prev:
            if cur==self.tail:
                self.tail = prev
            elif prev==self.tail:
                print('No node found with value {}'.format(val))
                f = False
                print('')
            if cur:   
                prev.next = cur.next
        else:
            self.head = cur.next
        if f:
            self.length -=1
        del cur

    
""" ###########################  play with the driver code! ###################################
print('')
s = LinkedList()
print(str(s))
for i in range(10):
    s.addnode(i)
print('')
s.traverse()
while(True):
    n = int(input('1 : traverse, 2 : delete, other wise : addnode : '))
    val = input('enter value : ')
    print('')
    if n==1:
        s.traverse()
    elif n==2:
        s.delete(int(val))
    else:
        s.addnode(int(val)) """
        
