class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        '''
        Initialize a variable to hold output variable
        Iterate through the given array
        Have a pointer pointing at the current value and compare it with the loop
        

        '''
        
        good_pairs = 0
        iterator = 1
        
        for number in range(len(nums)):
            
            while(iterator < len(nums)):
                
                if nums[number] == nums[iterator] and (number < iterator):
                    
                    good_pairs += 1
                
                iterator += 1
                
            iterator = number + 1
            
        return good_pairs
            
'''
Runtime: 32 ms, faster than 72.80'%' of Python3 online submissions for Number of Good Pairs.
Memory Usage: 14 MB, less than 29.26'%' of Python3 online submissions for Number of Good Pairs.

'''