'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        final_length = length = len(nums)
        count = 0  #iterator
        
        

        while(val in nums):
            if nums[count] == val:
                nums.pop(count)
                final_length = length - 1
            else:
                count += 1
        
        return final_length
                