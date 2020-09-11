'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        a_int = int(a,2)
        b_int = int(b,2)
        
        binary_sum = str(bin(a_int + b_int))
        
        return binary_sum[2:]