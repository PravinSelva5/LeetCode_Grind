'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
If the number of keys exceeds the capacity from this operation, evict the least recently used key.

Time Complexity for get and put is O(1)
Space Complexity is O(M), where M represents the capacity of the dequeue. The map and dequeue are bounded by the capacity given
----------
RESULTS
__________
Runtime: 500 ms, faster than 12.49% of Python3 online submissions for LRU Cache.
Memory Usage: 23.4 MB, less than 48.78% of Python3 online submissions for LRU Cache.
'''
from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.m = dict()
        self.deq = deque()
        
    def get(self, key: int) -> int:
        # Check if key is present in map, if not return -1
        # Move the key to the front of the deque
        # Return the value of our key from the map
        
        if key in self.m:
            value = self.m[key]
            self.deq.remove(key)
            self.deq.append(key)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Check if the key is in the map and is the map already filled to capacity?
            # If yes, remove the last element in the dequeue by popping it
            # Save new key value to dequeue
            # Push key,value pair to the front of the dequeue
        # If key is already in our map
        # Update the key's value and push it to the front of the dequeue
        
        if key not in self.m:
            if len(self.deq) == self.c:
                oldest = self.deq.popleft()
                del self.m[oldest]
        else:
                self.deq.remove(key)
        
        self.m[key] = value
        self.deq.append(key)
'''
# For fast lookups, you need to use maps
# For fast removals, we need a double ended queue (dequeue)
# Dequeues provide O(1) for append and pop operations
'''