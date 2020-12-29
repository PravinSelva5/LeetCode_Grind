'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

---------
 RESULTS
---------
Time Complexity: O(N)
Space Complexity: O(N)

Runtime: 24 ms, faster than 94.99% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.3 MB, less than 48.42% of Python3 online submissions for Valid Parentheses.


'''
class Solution:
    def isEqual(self, topElement, character):
        if topElement == '(' and character == ')':
            return True
        if topElement == '[' and character == ']':
            return True
        if topElement == '{' and character == '}':
            return True
        
    def isValid(self, s: str) -> bool:
        stack = []
        
        for character in s:
            
            if len(stack) != 0:
                topElement = stack[-1]
                
                if self.isEqual(topElement, character):
                    stack.pop()
                    continue
                
            stack.append(character)
            

        return len(stack) == 0