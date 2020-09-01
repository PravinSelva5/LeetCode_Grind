'''
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1
'''

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # Find the largest number in the array
        max_value = max(nums)
        counter = 0
        length = len(nums)
        
        for i in range(length):
            if max_value == nums[i]:
                max_index = i
                continue
            elif nums[i] * 2 <= max_value:
                counter += 1
        
        # Check to see if counter is equal to length of the list excluding the max value
        # if true, the index of the max value will be returned,
        # Otherwise, it will output -1
        
        if counter == length-1:
            return max_index
        else:
            return -1