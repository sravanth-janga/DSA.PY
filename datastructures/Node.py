# generic node class 
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

# A Node in typical binary tree
class BinaryNode(Node):
    def __init__(self,val):
        super().__init__(val)
        self.parent = None
        self.left = None
        self.right = None
