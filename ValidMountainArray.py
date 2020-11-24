'''
Given an array of integers arr, return true if and only if it is a valid mountain array

11/24/2020 15:41	Accepted	196 ms	15.5 MB	python3

Runtime: 196 ms, faster than 69.14`%` of Python3 online submissions for Valid Mountain Array.
Memory Usage: 15.5 MB, less than 8.92`%` of Python3 online submissions for Valid Mountain Array.
'''
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        
        # Check if length of array is equal to or greater than 3
        if len(arr) < 3:
            return False
        
        iterator = 1
        
        # Is array Strictly Increasing
        while iterator < len(arr) and arr[iterator] > arr[iterator - 1]:
            iterator += 1
        
        # Check if valid mountain criteria failed after first while loop
        if iterator == 1 or iterator == len(arr):
            return False
        
        # Check to see if array is Strictly Decreasing at this point
        while iterator < len(arr) and arr[iterator] < arr[iterator - 1]:
            iterator += 1
            
        # Check to see if iterator made it to the end of the given array
        return iterator == len(arr)