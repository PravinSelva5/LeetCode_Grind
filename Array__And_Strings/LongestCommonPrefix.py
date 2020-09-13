'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # Initialize values
        
        longest_prefix = []
        first_word = strs[0]
        j = 0
        temp = ''
        
        # If strs is empty, return ""
        if len(strs) == 0:
            return longest_prefix
        
        # Loop through first word to compare other letters
        for letter in range(len(first_word)):
            # Loop through each word and the words letter
            for i in range(1,len(strs)):
                
                while j <= len(strs[i]) and strs[letter] == strs[i][j]:
                    temp += strs[i][j]
                    j += 1
            
            longest_prefix.append(temp)
        
        return min(longest_prefix)