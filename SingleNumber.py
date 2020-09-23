class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        Create a dictionary that will maintain the number of occurences for each integer
        
        Run a for-loop through given list:
            if the current integer is present:
                add 1 to its key value
            else:
                append integer into dictionary and add 1 to its key value
        
        return key with value == 1
        '''
        
        dict_occurences = {}
        
        if len(nums) == 0:
            return 0
        
        for integer in nums:
            
            if (integer in dict_occurences):
                dict_occurences[integer] += 1
            
            else:
                dict_occurences[integer] = 1
        
        for i in dict_occurences:
            
            if dict_occurences[i] == 1:
                
                return i