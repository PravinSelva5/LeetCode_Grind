'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

-------
RESULTS
-------
Time Complexity: O(N*M)
Space Complexity: O(N*M)

Runtime: 32 ms, faster than 58.61% of Python3 online submissions for Unique Paths.
Memory Usage: 14.3 MB, less than 28.20% of Python3 online submissions for Unique Paths.

'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for x in range(m)] for y in range(n)] 
        
        # Fill first row elements with 1 because there is only one way to go through the first row which is moving all the way to the right
        for i in range(m):
            dp[0][i] = 1
        
        # Fill first columns elements with 1
        for i in range(n):
            dp[i][0] = 1
            
        
        for i in range(1,n):
            for j in range(1,m):
                
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]