'''
------------------------
Depth First Search (DFS)
------------------------
- graph/tree serching algorithm, recursive
- Always moves FORWARD till there are no other nodes in current path, else BACKTRACK
- can be implemented recursively or using a stack
- Time Complexity: O(V+E)  v = vertices/nodes
- Space Complexity: O(V)
'''

from collections import defaultdict

class DFS:
    def __init__(self):
        self.DFS = defaultdict(list)
    
    def insertEdge(self, v1, v2):
        self.DFS[v1].append(v2)
    
    def searchingLogic(self, startNode):
        visited = set()
        stack = []
        stack.append(startNode)

        while len(stack):
            cur = stack[-1]  # take the top element
            stack.pop()

            if cur not in visited:
                print(cur, end=" ")
                visited.add(cur)
            
            for vertex in self.DFS[cur]:
                if vertex not in visited:
                    stack.append(vertex)

g = DFS()
g.insertEdge(2,1)
g.insertEdge(2,5)
g.insertEdge(5,6)
g.insertEdge(5,8)
g.insertEdge(6,9)

g.searchingLogic(2)