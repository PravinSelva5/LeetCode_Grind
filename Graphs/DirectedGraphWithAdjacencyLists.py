'''
--------------------
 GRAPHS TERMINOLOGY
--------------------
Nodes: The objects whos relation are expressed by edges
Edges: connectors between nodes
Undirected Graph: The edges are all bi-directional, the edges do not point in any specific direction
Directed Graph: A graph where the edges are uni-directional, the edges point in a single direction
Weighted Graph: Each edge is assigned a weight or cost.
Cyclic Graph: A graph that has atleast one edge that starts from one node and ends at the same node.

'''
from collections import defaultdict

# Directed Graph with adjacency list

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def insertEdge(self, node1, node2):
        self.graph[node1].append(node2)
    
    def printGraph(self):
        for node in self.graph:
            for value in self.graph[node]:
                print(node, "=>", value)




g = Graph()

g.insertEdge(1,5)
g.insertEdge(5,2)
g.insertEdge(2,7)
g.insertEdge(7,1)

g.printGraph()
# The print method should output:
# 1 => [5]
# 5 => [2]
# 2 => [7]
# 7 => [1]