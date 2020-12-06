'''
Given two strings s and t, return the minimum window in s which will contain all the characters in t.
If there is no such window in s that covers all characters in t, return the empty string "".
Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

Runtime: 132 ms, faster than 35.36% of Python3 online submissions for Minimum Window Substring.
Memory Usage: 14.9 MB, less than 26.06% of Python3 online submissions for Minimum Window Substring.
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str: 
        len1 = len(s)
        len2 = len(t)
        
        if len1 < len2:
            return ""
        
        hashString = {}
        hashCharacters = {}
        
        # Add given characters in t to hash map
        for i in range(len2):
            hashCharacters[t[i]] = hashCharacters.get(t[i],0) + 1
        
        count = left = 0
        startIndex = -1
        minLen = 1000000
        
        for j in range(len1):

            hashString[s[j]] = hashString.get(s[j],0) + 1
            
            if hashCharacters.get(s[j]) is None:
                hashCharacters[s[j]] = 0
                
            # Check to see if current letter occurence is less than the occurence in patter
            if  hashCharacters.get(s[j]) != 0  and hashString.get(s[j]) <= hashCharacters.get(s[j]):
                count += 1

            # Contract window
            if count == len2:
                while hashString.get(s[left]) > hashCharacters.get(s[left]):
                    hashString[s[left]] -= 1
                    left += 1
                
                windowLen = j - left + 1
                if minLen > windowLen:
                    minLen = windowLen
                    startIndex = left

        if startIndex == -1:
            return ""
        
        return s[startIndex: startIndex + minLen]

        # Expand substring if not valid, move right pointer
        # Contract substring if valid, move the left pointer