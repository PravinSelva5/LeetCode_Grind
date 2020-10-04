class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # splice the array into two smaller arrays
        x_array = nums[:n]
        y_array = nums[n:]
        
        #final array
        output_array = []
        
#         for element in range(len(nums)):
            
#             if element < len(y_array):
#                 output_array.append(x_array[element])
#                 output_array.append(y_array[element])

#         return output_array
        
        for element in range(len(x_array)):
            output_array.append(x_array[element])
            output_array.append(y_array[element])
        
        return output_array