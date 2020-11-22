'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = j = 0
        length = len(nums)
        
        # Check how many zeros are present in the array
        
        for i in range(length):
            if nums[i] == 0:
                zeros += 1
        
        # Find unique values in array and append
        
        for i in range(length):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        
        #append zeros to the end of the array
        
        for i in range(j,length):
            nums[i] = 0
        
        return nums 

'''
SOLUTION 2
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        anchor = 0
        length = len(nums)

        for iterator in range(length):

            if nums[iterator] != 0:
                #temp = nums[anchor]
                #nums[anchor] = nums[iterator]
                #nums[iterator] = temp
                nums[iterator], nums[anchor] = nums[anchor], nums[iterator]
                anchor += 1
        
        return nums
            
            


'''
Time Complexity = O(2N) = O(N)
Space Complexity = O(N)


ANOTHER IMPLEMENTATION

11/21/2020 19:06	Accepted	44 ms	15.5 MB	python3

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        anchor = 0
        n = len(nums)
        
        for num in nums:
            if num != 0:
                nums[anchor] = num
                anchor += 1
        
        for zero in range(anchor,n):
            nums[zero] = 0
'''