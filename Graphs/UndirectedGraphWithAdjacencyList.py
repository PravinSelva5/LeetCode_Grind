from collections import defaultdict

'''
An undirected graph should look like

if this is true:   v1 => [v2, v3, v4]
then this needs to be true as well:  v2 => [v1], v3 => [v1], v4 => [v1]

'''
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def insertEdge(self,v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)
    
    def  printGraph(self):
        for node in self.graph:
            for value in self.graph[node]:
                print(node, "=>", value)


graph = Graph()

graph.insertEdge(1,5)
graph.insertEdge(1, 100)
graph.insertEdge(5,2)
graph.insertEdge(2,7)
graph.insertEdge(7,1)

graph.printGraph()

    

