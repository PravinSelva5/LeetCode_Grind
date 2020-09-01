'''
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = 0
        left_sum = 0
        length = len(nums) 
        index = 0
        
        if length == 0:
            return -1
        
        for i in range(length):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i+1:])
            
            if right_sum == left_sum:
                index = i
                return index
            else:
                index = -1
        
        return index