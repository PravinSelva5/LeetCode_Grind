'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

--------------
    RESULTS
--------------

Runtime: 24 ms, faster than 94.81% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 14.4 MB, less than 18.95% of Python3 online submissions for Letter Combinations of a Phone Number.

'''

class Solution:
    def backtrack(self,ans, numberPad, digits, combination, index ):
        if index > len(digits):
            return
        
        if len(combination) == len(digits):
            ans.append(combination[:])
            return
        
        currentDigit = digits[index]
        currentString = numberPad[currentDigit]
        
        for i in range(len(currentString)):
            self.backtrack(ans, numberPad, digits, combination+currentString[i], index+1)
    
    
    
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if digits == "":
            return ans
        
        numberPad = { '2': "abc", '3': "def", '4': "ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9': "wxyz" }
        
        self.backtrack(ans, numberPad, digits, "", 0)
        
        return ans