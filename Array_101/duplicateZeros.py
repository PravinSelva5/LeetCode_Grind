class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        array_length = len(arr)
        length = 0
        new_array = []
        final_arr = []
        
        for i in range(array_length):
            if(arr[i] == 0):
                new_array.append(arr[i])
                new_array.append(0)
                length += 2  
            else: 
                new_array.append(arr[i])
                length += 1
        
        for i in range(array_length):
            arr[i] = new_array[i]
        
        return arr