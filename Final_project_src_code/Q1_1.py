
import numpy as np
import networkx as nx
#import matplotlib.pyplot as plt

file = open("Data.csv")
M = np.loadtxt(file,delimiter=',')
#print(M)
H = nx.from_numpy_matrix(M)
#print(H)
pos = nx.spring_layout(H)
#H.remove_nodes_from(list(nx.isolates(H)))
nx.draw_networkx_nodes(H,pos,node_size=1)
nx.draw_networkx_edges(H,pos,width=0.3)

print("The number of isolated nodes are : ", nx.number_of_isolates(H))
print("The number of nodes are : ", nx.number_of_nodes(H))
print("The number of edges are : ", nx.number_of_edges(H))





