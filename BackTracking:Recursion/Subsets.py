'''
Given an integer array nums, return all possible subsets (the power set).
The solution set must not contain duplicate subsets.

*** 
What is a subset?
***
A set X is a subset of another set Y if all elements of the set X are elements in the set Y

----------
 RESULTS
----------
Time Complexity: O(N*2^N)
Space Complexity: O(N*2^N)

Runtime: 48 ms, faster than 6.19% of Python3 online submissions for Subsets.
Memory Usage: 14.4 MB, less than 23.73% of Python3 online submissions for Subsets.

''' 

class Solution:
    
    def solution(self,nums, ans, cur, index):
        if index > len(nums):
            return
        ans.append(cur[:])
        
        for i in range(index, len(nums)):
            if nums[i] not in cur:
                cur.append(nums[i])
                self.solution(nums, ans, cur, i)
                cur.pop()
                
    
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # Number of possible subsets can be obtained beforehand with --> 2 ** n equation
        # For example, [1,2,3] will have 2 ** 3 = 8 subsets
        
        ans = []
        cur = []
        self.solution(nums, ans, cur, 0)   # 4th parameter is the index
        return ans