'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
'''

class MovingAverage:
    
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = [0] * size
        self.front = 0
        self.counter = 0
        self.capacity = size
        self.Runningsum = 0

    def next(self, val: int) -> float:
        #once queue is full, this if statement wil work
        if self.counter >= self.capacity:
            self.queue[self.front] = val
            self.front = (self.front + self.counter + 1) % self.capacity
            self.Runningsum = sum(self.queue) / self.capacity
            return self.Runningsum
        
        self.queue[self.counter] = val
        self.counter += 1
        
        
        if self.counter == 1:
            return val
        
        self.Runningsum = sum(self.queue) / self.counter
        
        return self.Runningsum
        

"""
Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(size)
param_1 = obj.next(val)
"""