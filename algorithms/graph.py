import sys,os
sys.path.append('..')
sys.path.append('.')

from datastructures.graphs import Graph
from Errors.exceptions import Empty
from datastructures.queue import Queue
from datastructures.stack import Stack
############################################################

class Algo(Graph):
    """ 
    Implementations of many useful graph algorithms packed together in a class.
    Feel free to ovveride some of the functionalities as per your needs.
    List of Algorithms :
        . traversal :  Depth First Search, and Breadth First Search
        . topological ordering   (only on DAGs)  
        . bipartition check
        . strongly connected components
        . single-source shortest paths : dijstras, Bellman-Ford
        . all-pairs shortest paths : floyd-warshall

    """
    def __init__(self,n,Edges,verbose=False,type='directed',repr='list'):
        self.visited = None
        self.__status = None # status of the node [white,black,grey]
        self.__topo = None
        super().__init__(n, verbose, type, repr)
        print('processing the graph...')
        self.makeGraph(Edges)
        print("Build completed.")

    def Bfs(self,start):
        """
        starts bfs from the node start and traverses the graph.
        """
        self.visited = dict()
        q = Queue()
        q.append(start)
        self.visited[start]=1
        if self.repr==1: 
            while(len(q)):
                cur = q.pop()
                print(cur)
                if self.G.get(cur):
                    for c in self.G[cur]:
                        if self.visited.get(c):
                            continue
                        self.visited[c]=1
                        q.append(c)

        if self.repr==2:
            while(len(q)):
                cur = q.pop()
                print(cur)
                u = cur-1
                for i in range(self.n):
                    if self.visited.get(i+1):
                        continue
                    if self.G[u][i]:
                        self.visited[i+1]=1
                        q.append(i+1)

    def __get_adj_nodes(self,node):
        # returns the adjacent nodes of the given node.
        C = []
        if self.repr==1: 
            if self.G.get(node):
                for c in self.G[node]:
                    C.append(c)
        else:
            for i in range(self.n):
                if self.G[node-1][i]:
                    C.append(i+1)
        return C
    def Dfs(self):
        '''
        Initializes status of each node
        topological ordering of the nodes can accessed via get_order function.
        status is dictionary that keeps track of the nodes state.
        status == 1 ( not yet discovered)
        status ==2 ( discovered )
        status == 3 ( completed)
        This algorithm can also be used to check for any cycles in the directed graph
        It returns topological ordering of the nodes if exists.
        
        '''
        self.__status = dict()
        self.__topo = Stack()
        for i in range(1,self.n+1):
            self.__status[i]=1
        for i in range(1,self.n+1):
            if self.__status[i]!=1:
                continue
            self.__dfs_visit(i)
        if self.__topo:
            return self.__topo
        print('Topological ordering is not possible!')

    def __dfs_visit(self,node):
        self.__status[node]=2
        adj = self.__get_adj_nodes(node)
        for c in adj:
            if self.__status[c]==2:
                self.__topo=None
                continue
            if self.__status[c]!=1:
                continue
            self.__status[c]=2
            self.__dfs_visit(c)
        self.__status[node]=3
        if self.__topo!=None:
            self.__topo.append(node)

""" # BFS driver code
E = [[1,2],[1,3],[1,4],[4,2],[4,5],[2,3],[5,3]]
g = Algo(5,E,repr='list')
print(g.G)
top = g.Dfs()
while(top):
    print(top.pop()) """