'''
Given an array A of integers, return true if and only if it is a valid mountain array.

'''
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        peak = 0
        length = len(A) - 1
        
        #edge case 1
        if (len(A) < 3):
            return False
        
        #Find the highest number in the array
        for i in range(length):
            if A[i] > peak:
                peak = A[i]
        
        if peak == A[0]:
            return False

        #Checks if array is strictly increasing   
        i = 0
        while (A[i] < peak and i < length):
            if A[i] < A[i+1]:
                i += 1
            else:
                return False

        #Checks if array is strictly decreasing
        while (A[i] <= peak and i < length):
            if A[i] > A[i+1]:
                i += 1
            else:
                return False
        
        if i == length:
            return True
        