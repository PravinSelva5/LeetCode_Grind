"""
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        new_list = []
        
        digits = [str(i) for i in digits]
        int_val = int("".join(digits))
        int_val += 1
        
        for i in str(int_val):
            new_list.append(i)
        
        return new_list