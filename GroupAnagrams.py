'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

----------------------------------
Time Complexity = O(N * Mlong(M))
Space Complexity = O(N)
----------------------------------

Runtime: 80 ms, faster than 99.74% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.1 MB, less than 71.44% of Python3 online submissions for Group Anagrams.
'''

class Solution:
    def findHash(self, s):
        return ''.join(sorted(s))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        answer = []
        hashMap = {}        
        
        for s in strs:
            hashed = self.findHash(s)
            
            if ( hashed not in hashMap):
                hashMap[hashed] = []
            
            hashMap[hashed].append(s)
        
        for p in hashMap.values():
            answer.append(p)
        
        return answer