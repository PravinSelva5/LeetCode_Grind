'''
Dynamic Programming

A technqiue used to solve problems where you divide a problem ino sub-problems. The results from the sub-problems are saved for later use.

How do you know if the problem is a Dynamic Programming Problem?

1. Check if the problem is recursive
2. A lot of repeated states in the problem

You are trading memory for speed!

There are two approaches:

1. Top-Down
2. Bottom-Up
    - Start from the base cases
    - Use the previous results to find the next answer



----------------------------------------------------------------
LEETCODE QUESTION
----------------------------------------------------------------

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

--------
RESULTS
--------
Runtime: 32 ms, faster than 58.59% of Python3 online submissions for House Robber.
Memory Usage: 14.1 MB, less than 63.16% of Python3 online submissions for House Robber.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return 0
        
        # dp will contain the maximum money up to this house
        dp = [0] * n
        dp[0] = nums[0]
        
        for i in range(1, n):
            if i == 1:
                dp[i] = max(nums[0], nums[1])
            
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]