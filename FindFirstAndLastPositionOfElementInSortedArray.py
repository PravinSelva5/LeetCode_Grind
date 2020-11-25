'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Runtime: 84 ms, faster than 52.93% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 15.3 MB, less than 9.07% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.

11/25/2020 14:17	Accepted	84 ms	15.3 MB	python3
'''
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Array is sorted, think about binary search!
        # Time Complexity: log(N) because I'm using binary search
        # Space Complexity: O(1), no additional memory is created, Just constants such as         # the pointers
        # Find position of the first occurence first
        start_ptr = 0
        end_ptr = len(nums) - 1
        left = right = 0
        
        
        # Check if target is in array
        if (target in nums) == False:
            return [-1,-1]
        
        while start_ptr <= end_ptr:
            
            midpoint = (start_ptr + end_ptr) // 2
            
            if nums[midpoint] == target:
                
                if (midpoint - 1 >= 0 and nums[midpoint - 1] != target) or midpoint == 0:
                    
                    left = midpoint
                
                end_ptr = midpoint - 1
            
            elif nums[midpoint] > target:
                end_ptr = midpoint - 1
            
            else:
                start_ptr = midpoint + 1
        
        # Reset pointers
        start_ptr = 0
        end_ptr = len(nums) - 1
        
        # Finding last position of target
        while start_ptr <= end_ptr:
            
            midpoint = (start_ptr + end_ptr) // 2
            
            if nums[midpoint] == target:
                
                if midpoint == len(nums) - 1 or nums[midpoint + 1] != target:
                    right = midpoint
                    
                start_ptr = midpoint + 1
            
            elif nums[midpoint] > target:
                end_ptr = midpoint - 1
            
            else:
                start_ptr = midpoint + 1
        
        return [left, right]

s = Solution()
answer = s.searchRange([1], 1)
print(answer)


'''
11/25/2020 14:24	Accepted	80 ms	15.3 MB	python3

class Solution:
    
    def findLeftPosition(self, nums, target):
        start_ptr = 0
        end_ptr = len(nums) - 1
        left = 0
        
        while start_ptr <= end_ptr:
            
            midpoint = (start_ptr + end_ptr) // 2
            
            if nums[midpoint] == target:
                
                if (midpoint - 1 >= 0 and nums[midpoint - 1] != target) or midpoint == 0:
                    
                    left = midpoint
                
                end_ptr = midpoint - 1
            
            elif nums[midpoint] > target:
                end_ptr = midpoint - 1
            
            else:
                start_ptr = midpoint + 1
        return left
    
    def findRightPosition(self,nums, target):
        # Finding last position of target
        start_ptr = 0
        end_ptr = len(nums) - 1
        right = 0
        while start_ptr <= end_ptr:
            midpoint = (start_ptr + end_ptr) // 2
            if nums[midpoint] == target:
                
                if midpoint == len(nums) - 1 or nums[midpoint + 1] != target:
                    right = midpoint
                    
                start_ptr = midpoint + 1
            
            elif nums[midpoint] > target:
                end_ptr = midpoint - 1
            else:
                start_ptr = midpoint + 1
        
        return right
        
    
    
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Array is sorted, think about binary search!
        # Time Complexity: log(N) because I'm using binary search
        # Space Complexity: O(1), no additional memory is created, Just constants such as         # the pointers
        # Find position of the first occurence first
        
        # Check if target is in array
        if (target in nums) == False:
            return [-1,-1]
        
        left = self.findLeftPosition(nums, target)
        right = self.findRightPosition(nums, target)
        
        return [left, right]

        
'''