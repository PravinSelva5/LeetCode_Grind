'''
Breadth First Search

 - Searching algorithm
 - Traverses graph layer/level by layer/level
 - Moves horizontally and visits all nodes in the same layer before moving to the next layer.
 - You can use QUEUES to achieve this

 - Time Complexity: O(V+E)
 - Space Complexity: O(V)

'''
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def setEdge(self, node1, node2):
        self.graph[node1].append(node2)
    
    def bfs(self, startNode):
        visited = set()

        queue = []
        queue.append(startNode)

        visited.add(startNode)

        while queue:

            front = queue.pop(0)
            print(front, end=" ")

            for child in self.graph[front]:

                if child not in visited:

                    queue.append(child)
                    visited.add(child)


g = Graph()

g.setEdge(2,1)
g.setEdge(2,5)
g.setEdge(5,6)
g.setEdge(5,8)
g.setEdge(6,9)

g.bfs(2)