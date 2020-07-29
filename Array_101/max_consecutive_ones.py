'''
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total_ones = tmp = 0
            
        for number in nums:
            if number == 1:
                tmp += 1
            else:
                total_ones = max(total_ones, tmp)
                tmp = 0
        
        return max(total_ones,tmp)