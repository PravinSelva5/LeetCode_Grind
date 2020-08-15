'''
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

'''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        Max = nums[0]
        Second_Max = -10000000000000000
        Third_Max = -10000000000000000
        
        for i in nums:
            
            if i > Max:
                Third_Max = Second_Max
                Second_Max = Max
                Max = i
            
            elif i > Second_Max and i < Max:
                Third_Max = Second_Max
                Second_Max = i
                
            
            elif i > Third_Max and i < Second_Max:
                Third_Max = i
                continue
        
        if Third_Max == -10000000000000000: 
            return Max
        else:
            return Third_Max
