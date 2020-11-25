'''
Given a string s, find the length of the longest substring without repeating characters.

 - Sliding Window Technique

Runtime: 60 ms, faster than 69.05% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.4 MB, less than 5.93% of Python3 online submissions for Longest Substring Without Repeating Characters.

 11/25/2020 11:23	Accepted	60 ms	14.4 MB	python3

 TIME COMPLEXITY O(N)
 SPACE COMPLEXITY O(N)
'''

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        letter_map = {}
        left_ptr = right_ptr = longest_Substring = 0
        arr_len = len(s)
        
        while left_ptr < arr_len and right_ptr < arr_len:
            
            current_element = s[right_ptr]
            
            if current_element in letter_map:
                left_ptr = max(left_ptr, letter_map[current_element] + 1)
            
            letter_map[current_element] = right_ptr
            
            longest_Substring = max(longest_Substring,right_ptr - left_ptr + 1 )
            right_ptr += 1
            
        
        return longest_Substring

s = Solution()
string = "pwwkew"
answer = s.lengthOfLongestSubstring(string)
print(answer)