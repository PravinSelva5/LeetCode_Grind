'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Runtime: 116 ms, faster than 62.56% of Python3 online submissions for Contains Duplicate.
Memory Usage: 21.5 MB, less than 6.33% of Python3 online submissions for Contains Duplicate.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
         # I could sort the array and loop through to check if there's any repeated values
         # I could create a array that contains the given list as a set and compare the lengths of the two arrays
         # Another way is to use a hash map.
            
        m = {}
        
        for num in nums:
            # Check if number is already in our hash map
            if num in m:
                return True
            # Add to map if value not in it
            m[num] = 1
        
        return False