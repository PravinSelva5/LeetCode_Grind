'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

'''
class Solution:
    def isValid(self, s: str) -> bool:
            possible_values = { "(":")", "{": "}", "[": "]",")": "(", "]": "[",  "}": "{"}
            correct_order = ['(', '[', '{']
            temp_array = []
            
            for bracket in s:
                
                if (len(temp_array) > 0 and possible_values[bracket] == temp_array[- 1]):
                    temp_array = temp_array[:-1]
                    
                
                elif bracket not in correct_order:
                    return False
                
                else:
                        temp_array.append(bracket)
                
                
                # Checks to see if the temp_array is empty or not
                
            if (not temp_array):
                return True
            else:
                return False
                                     