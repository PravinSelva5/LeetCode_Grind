'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

-------------
  RESULTS
------------
Runtime: 60 ms, faster than 70.66% of Python3 online submissions for Min Stack.
Memory Usage: 18.5 MB, less than 17.18% of Python3 online submissions for Min Stack.
'''

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        
    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
            return
        
        currentMin = self.getMin()
        if currentMin == None or currentMin > x:
            currentMin = x
        self.stack.append((x, currentMin))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()