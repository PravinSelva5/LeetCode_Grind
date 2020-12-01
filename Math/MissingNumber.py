'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.


Time Complexity - O(N)
Space Complexity - O(1)

Runtime: 136 ms, faster than 37.28% of Python3 online submissions for Missing Number.
Memory Usage: 15.4 MB, less than 25.91% of Python3 online submissions for Missing Number.
'''
class Solution:
    def missingNumber(self, nums):
        
        '''
        To find the sum of elements from 0 to N, the following formula can be used --> [ n * (n + 1) / 2 ] Gauss formula
        
        - Find the intended sum with the gauss formula
        - calculate the sum of the given array
        - subtract the two and the missing value should our answer
        '''
        calc_sum = 0
        array_len = len(nums)
        intended_sum = ( array_len * ( array_len + 1 ) ) // 2
        
        # find the sum of the given array
        for num in nums:
            calc_sum += num
        
        return intended_sum - calc_sum