'''
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

 
Example 1:

Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: "aeiou"
Output: ""


Runtime: 28 ms, faster than 75.93% of Python3 online submissions for Remove Vowels from a String.
Memory Usage: 14.3 MB, less than 99.95% of Python3 online submissions for Remove Vowels from a String
'''

class Solution:
    def removeVowels(self, S: str) -> str:
        """
        - Create a vowel_list that contains the possible vowels 
        
        - Iterate through the given string
            - If current letter IN vowel_list
                - pop the letter out
            - ELSE
                CONTINUE WITH the loop
        """
        
        vowel_list = ['a', 'e', 'i', 'o', 'u']
        output = ""
        
        for letter in S:
            
            if letter not in vowel_list:
                
                output += letter
            
            else:
                continue
                
        return output
