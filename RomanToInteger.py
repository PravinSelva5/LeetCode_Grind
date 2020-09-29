class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        - Initialize a dictionary with the seven different symbols & their integer value
        
        - Loop through each letter
            
            - if condition, to check if first letter is < than second
                - negate its value 
            - else
                sum up the values
        
        '''
        
        roman_to_integer_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000        
        }
        
        total_sum = 0
        
        for symbol in range(len(s)):
            
            if (symbol < len(s)-1) and (roman_to_integer_dict[s[symbol]] < roman_to_integer_dict[s[symbol+1]]):
                total_sum +=  roman_to_integer_dict[s[symbol]] * -1
            
            else:
                total_sum += roman_to_integer_dict[s[symbol]]
                
        return total_sum
        
        