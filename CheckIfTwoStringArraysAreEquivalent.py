'''
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.


11/24/2020 21:23	Accepted	28 ms	14.4 MB	python3
'''
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        full_word_1 = ""
        full_word_2 = ""
        
        # Concatenate list 1
        for letter in word1:
            full_word_1 += letter
        
        # Concatenate list 2
        for letter2 in word2:
            full_word_2 += letter2
        
        # Check if the concatenation is the same
        return full_word_1 == full_word_2