# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.


class Solution:
    def singleNumber(self, nums) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        Runtime: 124 ms, faster than 85.10% of Python3 online submissions for Single Number.
        Memory Usage: 16.7 MB, less than 5.34% of Python3 online submissions for Single Number.
        '''
        unique_values = set(nums)
        unique_sum = 0
        actual_sum = 0
        
        # Calculate unique sum
        for num in unique_values:
            unique_sum += num
        
        # Calculate actual sum of nums
        for val in nums:
            actual_sum += val
            
        
        return 2*unique_sum - actual_sum

s = Solution()
answer = s.singleNumber([2,2,1])
print(answer)