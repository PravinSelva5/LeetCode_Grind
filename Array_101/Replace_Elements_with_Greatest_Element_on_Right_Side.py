'''
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

IN-PLACE OPERATIONS HELP REDUCE THE SPACE COMPLEXITY.
IN-PLACE OPERATIONS MODIFY THE INPUT DATA STRUCTURE AND RETURN IT 
'''


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        length = len(arr) - 1
        max_value = 0
        temp = -1
        
        for i in range(length,-1,-1):
            max_value = max(temp, arr[i])
            arr[i] = temp
            temp = max_value
        
        return arr