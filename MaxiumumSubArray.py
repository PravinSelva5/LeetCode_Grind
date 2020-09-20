
'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize two sum variables. Once is the max sum and the other is current sum
        current_sum = 0
        maximum_sum = nums[0]
        
        #Edge case
        if len(nums) == 1:
            return maximum_sum
        
        # Iterate through the length of the array given, 0 to n
        for digit in nums:
            # If current sum is negative, reset it to 0
            if current_sum < 0:
                current_sum = 0
            
            # Add current sum and current integer together
            current_sum += digit
            
            # Update the maximum between the current sum and the previous max value
            maximum_sum = max(maximum_sum, current_sum)
        
        return maximum_sum