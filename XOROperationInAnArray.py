'''
Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.
'''
from typing import List

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        
        # Creating nums array
        for i in range(n):
            nums.append(start + 2 * i)
            
        x = 0
        
        for number in nums:
            x ^= number
        
        return x

s = Solution()
answer = s.xorOperation(4,3)
print(answer)