from Node import BinaryNode
from stack import Stack

class MaxHeap:
    def __init__(self):
        self.root = None
        self.nonleaves = None
        self.list = [None]
        self.array = [None]  # stores the reference for the nodes as they are appended !
        self.__str__()

    # my dets!
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
    
    # Function responsible for maintaining the max heap property
    def Max_Heapify(self,node):
        L = node.left
        R = node.right
        Largest = node
        if L and L.val>Largest.val:
            Largest=L
        if R and R.val>Largest.val:
            Largest = R 
        if Largest!=node:
            self.swap(node,Largest)
            self.Max_Heapify(Largest)
    
    # swaps parent/anscestor with it's child/descendant
    def swap(self,parent,child):
        lchild = child.left
        superp = parent.parent 
        rchild = child.right
        R = parent.right
        L = parent.left
        if parent.left==child:  
            parent.parent = child 
            child.left = parent
            if R:
                child.right = R  
                R.parent = child
        elif parent.right==child:
            child.right = parent
            parent.parent = child
            if L:
                child.left = L 
                L.parent = child
        else:
            parent.parent = child.parent

       
        child.parent = superp
        if superp==None:
            self.root = child
        parent.left = lchild
        parent.right = rchild
        if lchild:
            lchild.parent = parent
        if rchild:
            rchild.parent = parent
    
    # method get stack of non leaves
    def get_non_leaves(self,node):
        if node.left or node.right:  # checks if the node has atleast one child
            self.nonleaves.append(node)
            
            if node.left:
                self.get_non_leaves(node.left)
            if node.right:
                self.get_non_leaves(node.right)
    
    # Builds max head
    def Build(self):
        self.nonleaves = Stack()
        self.get_non_leaves(self.root)
        print(len(self.nonleaves),'this is the length')
        while(self.nonleaves):
            cur = self.nonleaves.pop()
            self.Max_Heapify(cur)
    # append values to the head
    # appends nodes so that it forms a complete binary tree-
    def append(self,val):
        node = BinaryNode(val)
        self.list.append(node)
        i = len(self.list)-1
        node.parent = self.list[i//2]
        if self.root:
            if (i%2):
                self.list[i//2].right = node
            else:
                self.list[i//2].left = node
        else:
            self.root = node
        # while(cur):
        #     prev = cur
        #     if cur.val<val:
        #         cur = cur.right
        #     else:
        #         cur = cur.left
        # if prev:
        #     if prev.val<val:
        #         prev.right = node
        #     else:
        #         prev.left = node     
        # else:
        #     self.root = node    

H  = MaxHeap()
for i in range(10):
    H.append(i)

print(H.root.val)
H.Build()

print([c.val for c in H.list[1:]])
print(H.root.val)