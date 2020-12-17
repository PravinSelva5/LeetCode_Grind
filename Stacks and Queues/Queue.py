'''
- Linear data structure that has the order of First In First Out (FIFO)

- Enqueue, Front, Dequeue all have O(1)
'''

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, input):
        self.queue.append(input)
    
    def front(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return "Empty Queue"
    def dequeue(self):
        if len(self.queue) != 0:
            self.queue.pop(0)
        else:
            return "Empty Queue"

