'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

-----------------------
Clarification:
-----------------------
What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

'''

'''
SOLUTION 1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
'''

'''
SOLUTION 2: If you can't use python's find function
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # Edge Case
        
        if needle not in haystack:
            return -1
        
        # Initializing indexes
        len_haystack = len(haystack)
        len_needle = len(needle)
        
        # looping through input
        
        for i in range(len_haystack - len_needle + 1):
            if needle == haystack[i:i+len_needle]:
                return i
                

