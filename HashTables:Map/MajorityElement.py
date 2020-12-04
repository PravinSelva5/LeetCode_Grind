'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

----------------------
Time Complexity: O(N)
----------------------
Space Complexity: O(N)
----------------------


Runtime: 176 ms, faster than 20.76% of Python3 online submissions for Majority Element.
Memory Usage: 15.5 MB, less than 13.12% of Python3 online submissions for Majority Element.
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        occurences = {}
        
        # Loop through given array and add values & occurences to map
        for num in nums:
                occurences[num] = occurences.get(num, 0) + 1
                
        # Loop through map and find the value with occurences > n/2
        for occurence in nums:
            
            if occurences[occurence] > len(nums) /2:
                return occurence