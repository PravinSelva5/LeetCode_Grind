'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''

class Solution:
    def backtrack(self,)
    
    
    
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if digits == "":
            return ans
        
        numberPad = { 2: "abc", 3: "def", 4: "ghi", 5:"jkl", 6:"mno", 7"pqrs", 8:"tuv", 9: "wxyz" }
        
        backtrack(ans, m, digits, combination="", index=0)
        
        return ans