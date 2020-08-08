'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # pointers that will be used to keep track of the current element and unique element
        j = 0 
        if (len(nums) == 0): return 0
        for i in range(1,len(nums)):
            
            if (nums[i] != nums[j]):
                j += 1
                nums[j] = nums[i]
        
            
        return j+1