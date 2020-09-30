class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        - Assign the length of the list to a variable 
        - Loop through given list
             - If current value present in nums
                - continue
            - return the value
        '''
        
        len_nums = len(nums)
        nums.sort()
        for number in range(len_nums+1):
            if number not in nums:
                return number
        
        