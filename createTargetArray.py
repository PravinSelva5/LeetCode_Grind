'''
Create Target Array in the Given Order

Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

10/15/2020 22:00	Accepted	28 ms	13.9 MB	python3
'''
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        iterator = 0
        output_array = []
        temp = []
        
        for number in nums:
            
            # Check if output array contains value at index
            if iterator < len(index):
                
                output_array.insert(index[iterator], number)
                
            iterator += 1
        
        
        return output_array