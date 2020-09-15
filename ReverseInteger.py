'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

'''

class Solution:
    def reverse(self, x: int) -> int:
        # Create an empty list
        # Iterate through given list from -1 to the beginning & avoid -(ve) sign
        # Add the value to the new list
        # Convert list to int
        # if given int was negative, return -ve value
        
        empty_string = ''
        range_min = -2 ** 31
        range_max = (2 ** 31) -1
        string = str(x)
        len_integer = len(string)-1
        
        for i in range(len_integer, -1, -1):
            
            if string[i] != '-':
                empty_string += string[i]
            
        # Convert list of strings to an integer
        
        if int(empty_string) > range_max or int(empty_string) < range_min:
            return 0
        elif x < 0:
            return -1 * int(empty_string)
        else:
            return int(empty_string)