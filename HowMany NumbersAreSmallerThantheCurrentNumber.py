'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
Return the answer in an array.

10/11/2020 22:42	Accepted	420 ms	14.3 MB	python3
'''

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        # Create an empty dictionary
        occurences = {}
        iterator = 1
        anchor = 0
        counter = 0
        # Loop through given list and append values to dict
        for i in nums:
            occurences[i] = 0
        
        # Loop through nums
        while(anchor < len(nums)):
            
            if iterator == len(nums)-1:
                occurences[nums[anchor]] = counter
                anchor += 1
                
            elif  iterator <= len(nums) and nums[anchor] > nums[iterator]:
                counter += 1
                iterator += 1
                
            else:
                iterator += 1
                
                
        print(occurences)