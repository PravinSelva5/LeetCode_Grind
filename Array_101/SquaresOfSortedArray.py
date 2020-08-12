'''
SOLUTION 1


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        squared_array  = []
        
        for i in range(len(A)):
            squared_array.append(A[i] ** 2)
        
        return (sorted(squared_array))
'''

'''
SOLUTION 2
'''

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        length = len(A)
        i =  0
        j = length - 1
        
        output = [0] * length
        
        while (i < length and j >= i):
            anchor = j - i
            if abs(A[i]) > A[j]:
                output[anchor] = A[i] ** 2
                i += 1
            
            else:
                output[anchor] = A[j] ** 2
                j -= 1
        
        return output