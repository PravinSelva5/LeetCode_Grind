#---------------------------------------------------------------------# 
#  28/29 of Test Cases passed. Time Limit Exceeded for the last case
#  Need to leverage a hash map
#---------------------------------------------------------------------#

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                number1 = target - nums[i]
                if (nums[j] == number1 and i != j):
                    return i,j