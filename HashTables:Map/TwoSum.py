'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Runtime: 48 ms, faster than 73.88% of Python3 online submissions for Two Sum.
Memory Usage: 14.4 MB, less than 86.23% of Python3 online submissions for Two Sum.

Complexity:
-----------
Time Complexity = O(N)
Space Complexity = O(N)
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        
        for num in range(len(nums)):
            
            goal = target - nums[num]
            
            if goal in Map:
                return [num, Map[goal]]
            
            Map[nums[num]] = num