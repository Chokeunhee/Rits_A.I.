
import numpy as np
import networkx as nx
from collections import defaultdict

class Graph_build:
    def __init__ (self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
def BFS_SP(graph, start, goal): 
    explored = []      
    queue = [[start]]       
    
    if start == goal: 
        print("Same Node") 
        return      
    
    while queue: 
        path = queue.pop(0) 
        node = path[-1] 
        
        if node not in explored: 
            neighbours = graph[node] 
            
            for neighbour in neighbours: 
                new_path = list(path)
                new_path.append(neighbour) 
                queue.append(new_path) 
                
                if neighbour == goal: 
                    print("Shortest path = ", *new_path)
                    print("Distance = ",len(new_path)-1)
                    return
            explored.append(node)
    
    print("path doesn't exist :(") 
    return

file = open("Data.csv")
M = np.loadtxt(file,delimiter=',')
H = nx.from_numpy_matrix(M)
Edgelist =H.edges()
X = [x for x, y in Edgelist]
Y = [y for x, y in Edgelist]        
g = Graph_build(3013)
for i in range (len(X)):
    g.addEdge(X[i]+1,Y[i]+1)
    g.addEdge(Y[i]+1,X[i]+1)
graph = g.graph
BFS_SP(graph,27,1445)


