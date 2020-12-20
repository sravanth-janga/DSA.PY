import sys,os
sys.path.append(os.path.join('.'))
sys.path.append(os.path.join('..'))


# set verbose to False to avoid my info

#################################### MAX HEAP ################################################
class MaxHeap:
    def __init__(self,verbose=False):
        self.list = [None]
        self.heap_size = 0
        self.nxt = 0
        if verbose:
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
    def Max_Heapify(self,index):
        L = self.left(index)
        R = self.right(index)
        Max = index
        if L<=self.heap_size and self.list[Max]<=self.list[L]:
            Max = L 
        if R<=self.heap_size and self.list[Max]<=self.list[R]:
            Max = R  
        if Max != index:
            self.swap(Max, index)
            self.Max_Heapify(Max)
    # swaps two values
    def swap(self,i,j):
        self.list[i],self.list[j] = self.list[j],self.list[i]


    # heap sort alogrithm ascending
    def sort(self):
        hs = self.heap_size
        self.Build()
        for i in range(hs,1,-1):
            self.swap(i, 1)
            self.heap_size -=1
            self.Max_Heapify(1)
        self.heap_size = hs
    # Builds max heap
    def Build(self):
    # append values to the head
        for i in range(self.heap_size//2,0,-1):
            self.Max_Heapify(i)

    # appends nodes so that it forms a complete binary tree-
    def add(self,val):
        if self.nxt == self.heap_size+1:
            self.list[self.nxt] = val
        else:
            self.list.append(val)
        self.heap_size +=1
    # returns parent,leftchild, rightchild of node at index
    def parent(self,index):
        return index//2

    def left(self,index):
        return 2*index

    def right(self,index):
        return (2*index) + 1

################################## MIN HEAP ######################################################


class MinHeap:
    def __init__(self,verbose=False):
        self.list = [None]
        self.heap_size = 0
        self.nxt = 0
        if verbose:
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
    def Min_Heapify(self,index):
        L = self.left(index)
        R = self.right(index)
        Max = index
        if L<=self.heap_size and self.list[Max]>=self.list[L]:
            Max = L 
        if R<=self.heap_size and self.list[Max]>=self.list[R]:
            Max = R  
        if Max != index:
            self.swap(Max, index)
            self.Min_Heapify(Max)
    # swaps two values
    def swap(self,i,j):
        self.list[i],self.list[j] = self.list[j],self.list[i]


    # heap sort alogrithm desc
    def sort(self):
        hs = self.heap_size
        self.Build()
        for i in range(hs,1,-1):
            self.swap(i, 1)
            self.heap_size -=1
            self.Min_Heapify(1)
        self.heap_size = hs
    # Builds max heap
    def Build(self):
    # append values to the head
        for i in range(self.heap_size//2,0,-1):
            self.Min_Heapify(i)

    # appends nodes so that it forms a complete binary tree-
    def add(self,val):
        if self.nxt == self.heap_size+1:
            self.list[self.nxt] = val
        else:
            self.list.append(val)
        self.heap_size +=1
    # returns parent,leftchild, rightchild of node at index
    def parent(self,index):
        return index//2

    def left(self,index):
        return 2*index

    def right(self,index):
        return (2*index) + 1


""" #  driver code for testing 
H  = MinHeap(verbose=False) # replace MinHeap with MaxHeap to test max heap!
for i in range(10):
    H.add(i)
print(H.list)
H.add(10000)
H.add(200000000000)
H.add(10000000)
H.sort()
print(H.list) """