
import numpy as np
import networkx as nx
from collections import defaultdict


class Graph:
    
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def printAllPathsUtil(self,u,d,visited,path):
            
        visited[u]=True
        path.append(u)
        if u == d:
            if len(path) < 400:
                print(path)
                print("")
        else:
            for i in self.graph[u]:
                if visited[i]==False:
                    self.printAllPathsUtil(i,d,visited,path)
        
        path.pop()
        visited[u]=False

    
    def printAllPaths(self,s,d):
        visited = [False]*(self.V)
        path = []
        self.printAllPathsUtil(s,d,visited,path)

file = open("Data.csv")
M = np.loadtxt(file,delimiter=',')
H = nx.from_numpy_matrix(M)
Edgelist =H.edges()
X = [x for x, y in Edgelist]
Y = [y for x, y in Edgelist]        
g = Graph(3013)
for i in range (len(X)):
    g.addEdge(X[i]+1,Y[i]+1)
    g.addEdge(Y[i]+1,X[i]+1)
s = 27 ; d = 1445
print ("Following are all different paths from % d to % d :" %(s, d)) 


g.printAllPaths(s, d)


                 