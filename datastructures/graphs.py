import sys,os
sys.path.append(os.path.join('.'))
sys.path.append(os.path.join('..'))

from Errors.exceptions import Empty


class Graph:

    """
    Graph data structure which supports :
    1. adjacency list, and matrix representations.
    2. weighted and unweighted.
    3. directed and undirected.

    Note :
            Weighted graphs are represented using adjacency matrix

    Parameters :
        **  n : specifies the number of nodes in the graph, where nodes are numbered from 1 to n.
            * accepted vals : positive integers

        **  type : specifies the type of graph directed | undirected 
            * default : directed    
            * accepted vals : directed, undirected'

        **  repr : specifies the representation adjacency list | matrix
            * default : list
            * accepted vals : list, mat

        """
    GD = {
        'directed':1,
        'undirected':2,
        'list':1,
        'mat':2
    }
    def __init__(self,n,verbose=False,type='directed',repr ='list'):

        if not(n>0 and isinstance(n,int)):
            raise Empty("Specified value {} is not allowed! \n use help functiont to know about config".format(n))

        if not(type =='directed' or type=='undirected'):
            raise Empty("Specified type {} is not allowed! \n use help functiont to know about config".format(type))


        if not(repr=='list' or repr=='mat'):
            raise Empty("Specified repr {} is not allowed! \n use help functiont to know about config".format(repr))
        self.G = dict()
        if verbose:
            self.__str__()
        self.type = Graph.GD.get(type)
        self.repr = Graph.GD.get(repr)
        self.n = n  
        if self.repr==1:
            self.G = dict() 
        else:
            self.G = [[0 for _ in range(n)] for __ in range(n)] # empty nXn array to represent the graph


    def __str__(self):
        print( """       
        
            #####################################################################
            #                                                                   #
            # author   : Sravanth Janga,                                        #              
            # github   : https://github.com/sravanth-janga,                     #
            # linkedin : https://www.linkedin.com/in/sravanth-reddy-22771816a/  #
            #                                                                   #
            #   call help to know configuration dets                            #
            #                                                                   #
            # ###################################################################

            
        """)
    def __AddEdge(self,E):
        """
        E : An edge in the graph
        format :
            Weighted :
                E = [u,v,w] 
                edge between node u, and node v
                w is the weight of the edge
            UnWeighted :
                E = [u,v]

        """
        w = None
        if len(E)==2:
            u,v = E   
        else:
            u,v,w = E  
        if self.repr ==1:
            if w is not None:
                print('overriding the configuration, setting the representation to adjacency matrix')
                self.G = [[0 for _ in range(self.n)] for __ in range(self.n)]
                self.repr =2
            else:
                if self.G.get(u):
                    self.G[u].append(v)
                else:
                    self.G[u]=[v]
                if self.type==2:
                    if self.G.get(v):
                        self.G[v].append(u)
                    else:
                        self.G[v]=[u]  


        if self.repr==2:
            if w is not None:
                pass
            else:
                w = 1
            self.G[u-1][v-1]=w 
            if self.type==2:
                self.G[v-1][u-1]=w 

    def makeGraph(self,Edges):
        """
        Makes the graph according to the specified configuration.
     
        => self.G is actual graph 

        Note :
        adj list:
                if Graph is in the adj list format then self.G is a dictionray
                each key is the node
                if a node has any adjacent nodes then they are stored in the list,
                and are associated with the node as a key value pairs

            Ex:
                self.G = {
                    node : [node1,node2,node3,...,nodek]
                } 

        Edges : list of edges 
        where,
        E : An edge in the graph
        format :
            Weighted :
                E = [u,v,w] 
                edge between node u, and node v
                w is the weight of the edge
            UnWeighted :
                E = [u,v]
            
        """
        for E in Edges:
            self.__AddEdge(E)



"""# driver code !
WA = [[1,2,10],[2,3,2],[4,2,1]]
A = [[1,2],[2,3],[4,2]]
g=Graph(4)
gw = Graph(4)
g.makeGraph(A)
print('----------- unweighted graph ---------------------')
print(g.G)

print('------------weighted graph -----------------------')
gw.makeGraph(WA)
print(gw.G) """
