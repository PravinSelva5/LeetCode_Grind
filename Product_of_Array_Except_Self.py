class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        left_array, right_array, output_array = [0] * length, [0] * length, [0] * length
        
        left_array[0] = 1
        
        for i in range(1, length):
            
            left_array[i] = nums[i-1] * left_array[i-1]
        
        right_array[length - 1] = 1
        
        for i in reversed(range(length-1)):
            right_array[i] = nums[i+1] * right_array[i+1]
        
        
        for i in range(length):
            output_array[i] = left_array[i] * right_array[i]
        
        return output_array
            