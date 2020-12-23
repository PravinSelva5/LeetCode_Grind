'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order. The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

--------------
    RESULTS
--------------
Runtime: 80 ms, faster than 63.52% of Python3 online submissions for Combination Sum.
Memory Usage: 14.3 MB, less than 30.57% of Python3 online submissions for Combination Sum.
'''

# -------------------------------------------------------------------------------------------------------------------------------------------------------- #
        # If you ever see questions asking for all the possible combinations, subsets --> You should think of BACKTRACKING/RECURSION
# -------------------------------------------------------------------------------------------------------------------------------------------------------- #

class Solution:
    def searchCombinationSum(self, candidates, answer, currentList, target, index, summation):
        if summation == target:
            answer.append(currentList[:])
        
        elif summation < target:
            n = len(candidates)
            
            for i in range(index, n):
                currentList.append(candidates[i])
                # Add element to current list and check if it sums to the target
                self.searchCombinationSum(candidates, answer, currentList, target, i, summation + candidates[i])
                currentList.pop()
            return
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        answer = []
        currentList = []
        self.searchCombinationSum(candidates, answer, currentList, target, 0, 0)
        
        return answer
        