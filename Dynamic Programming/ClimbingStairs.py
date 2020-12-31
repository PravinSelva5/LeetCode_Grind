'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

---------
RESULTS
---------
Time Complexity: O(N)
Space Complexity: O(N)

Runtime: 28 ms, faster than 77.72% of Python3 online submissions for Climbing Stairs.
Memory Usage: 14 MB, less than 97.16% of Python3 online submissions for Climbing Stairs.
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n==1:
            return 1
        
        dynamicProgArray = [0] * (n + 1)  # we're counting from 1 not 0
        
        dynamicProgArray[1] = 1
        dynamicProgArray[2] = 2
        
        
        for i in range(3, n + 1):
            
            dynamicProgArray[i] = dynamicProgArray[i-1] + dynamicProgArray[i-2]
        
        return dynamicProgArray[n]