class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        # temporary number holder
        output_array = []
        temp = 0
        
        for i in nums:
            # Add value to temp array
            # append to output array
            temp += i
            output_array.append(temp)
        
        
        return output_array
            
        