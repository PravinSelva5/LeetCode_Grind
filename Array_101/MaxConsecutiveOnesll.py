'''
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

** Needed Help for this one **
'''



class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        previous = -1
        current = maxLen = 0
        
        for i in nums:
            
            if i == 0:
                maxLen = max(maxLen, previous + 1 + current)
                previous, current = current, 0
            else:
                current += 1
        
        return max(maxLen, previous + 1 + current)