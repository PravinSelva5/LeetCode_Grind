'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
'''

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        length = len(A)
        i =  0
        j = length - 1
        
        while(i < length and j >= i):
            
            if A[i] % 2 == 0:
                i += 1
            
            else:
                A[i], A[j] = A[j], A[i]
                j -= 1
                
        return A