'''
------------
QUESTION
-------------
Given two binary strings a and b, return their sum as a binary string.


Runtime: 36 ms, faster than 38.12% of Python3 online submissions for Add Binary.
Memory Usage: 14.2 MB, less than 17.18% of Python3 online submissions for Add Binary.

'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        answer = []
        carry = 0 
        i,j = len(a)-1, len(b)-1
        
        while i >= 0 or j>= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            
            if j >= 0:
                total += int(b[i])
                j -= 1
            
            answer.append(str(total%2))
            
            carry = total // 2
            
        return ''.join(reversed(answer))