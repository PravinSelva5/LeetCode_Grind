'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
        
        -  two pointer technqiue
            - one pointing at the front
            - one pointing at the end of the array
        - loop as long as the left pointer is less than the right pointer
        - find the area of the two heights the pointers are pointing to
        - move the pointer that's pointing to the smaller height

    Runtime: 168 ms, faster than 49.38% of Python3 online submissions for Container With Most Water.
    Memory Usage: 16.5 MB, less than 11.77% of Python3 online submissions for Container With Most Water.

    11/24/2020 20:38	Accepted	168 ms	16.5 MB	python3
'''
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Pointers and variables
        front_ptr = 0
        back_ptr = len(height) - 1
        max_area = 0
        
        # Check for the highest area as long as front_ptr < back_ptr
        while ( front_ptr < back_ptr):
            
            max_area = max(max_area, min(height[front_ptr], height[back_ptr])  * (back_ptr - front_ptr) )
            
            # Decide which pointer to increment or decrement
            if height[front_ptr] > height[back_ptr]:
                back_ptr -= 1
            else:
                front_ptr += 1
        
        return max_area
    
s = Solution()
answer = s.maxArea([4,3,2,1,4])
print(answer)