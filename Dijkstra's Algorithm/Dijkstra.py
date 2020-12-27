'''
- Usually used to find the shortest path between 2 nodes in a graph
- Time Complexity: O(|E| log |V|)


-------------------------------------
Network Delay Time LeetCode Question
-------------------------------------

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

-------------------
     RESULTS
-------------------
Runtime: 428 ms, faster than 97.94% of Python3 online submissions for Network Delay Time.
Memory Usage: 16.2 MB, less than 52.68% of Python3 online submissions for Network Delay Time.
'''

from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        g = collections.defaultdict(list)
        
        
        for u,v,cost in times:
            g[u].append((cost,v))
        
        min_heap = [(0,K)]
        
        visited = set()
        
        distance = { i:float('inf') for i in range(1, N+1)}
        distance[K] = 0
        
        while min_heap:
            
            cur_distance, u = heapq.heappop(min_heap)
            
            if u in visited:
                continue
            visited.add(u)
            
            if len(visited) == N:
                return cur_distance
            
            for direct_distance,v in g[u]:
                if cur_distance + direct_distance < distance[v] and v not in visited:
                    distance[v] = cur_distance + direct_distance
                    heapq.heappush(min_heap, (distance[v], v))
        
        return -1        