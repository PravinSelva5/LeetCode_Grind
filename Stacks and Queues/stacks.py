'''
- Linear data structure which has the order of last in first out (LIFO)
- pop removes the top element from the stack and shows the value 
- top shows the value of the top element
- push, pushes a new element to the stack (array)

----------------------------------------------------------------
Time Complexity for pop, push, and top for a stack are all O(1)
----------------------------------------------------------------



'''

class PlateStack:

    def __init__(self):
        self.stack = []
    
    def push(self,x ):
        self.stack.append(x)
    
    def pop(self):
        if len(self.stack > 0):
            self.stack.pop()
        else:
            return "Empty Stack"

    def top(self):
        if len(self.stack > 0):
            return self.stack[-1]
        else:
            return "Empty Stack"
        
    def getLen(self):
        return len(self.stack)