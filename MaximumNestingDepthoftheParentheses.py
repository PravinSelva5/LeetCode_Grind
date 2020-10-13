'''
A string is a valid parentheses string (denoted VPS) if it meets one of the following:

It is an empty string "", or a single character not equal to "(" or ")",
It can be written as AB (A concatenated with B), where A and B are VPS's, or
It can be written as (A), where A is a VPS.
We can similarly define the nesting depth depth(S) of any VPS S as follows:

depth("") = 0
depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's
depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS represented as string s, return the nesting depth of s.

---------------------
 SUBMISSION RESULTS
---------------------
Time Submitted      Status     Runtime  Memory     Language
10/12/2020 23:35	Accepted	32 ms	14.2 MB	   python3

'''
class Solution:
    def maxDepth(self, s: str) -> int:
        # Counter will count the depth of the paranthesis
        depth = 0
        counter = 0 
        depth_queue = []
        
        # Loop through the given string
        for letter in s:
            
            # Compare each letter with open parenthesis
            if letter == '(':
                depth_queue.append(letter)
                counter += 1
            
            # Check if the letter is a closed bracket
            if letter == ')':
                
                del depth_queue[-1]
                
                if counter > depth:
                    depth = counter
                
                counter -= 1
            
            else:
                continue
        
        return depth