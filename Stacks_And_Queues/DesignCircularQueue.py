class MyCircularQueue:
    
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [0] * k
        self.front = 0 #keeps track of the current head of the queue
        self.counter = 0 #keeps track of the current length of the queue
        self.capacity = k 
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        
        if self.counter == self.capacity:
            return False
        self.queue[(self.front + self.counter) % self.capacity] = value
        self.counter += 1
        return True
        
    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        
        if self.counter == 0:
            return False
        self.front = (self.front + 1) % self.capacity
        self.counter -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.counter == 0:
            return -1
        return self.queue[self.front]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.counter == 0:
            return -1
        return self.queue[(self.front + self.counter - 1) % self.capacity]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.counter == 0
            
        
    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.counter == self.capacity
