class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        - Create a temporary variable that will hold the current letter
        - Create a counter variable that will keep track of the opposite element
        - Iterate through the given list
            - swap first and last characters
            - decrement counter variable 
        - return List
        """
        
        temp_var = ""
        counter_index = len(s) - 1
        
        for character in range(len(s)):
            
            if counter_index > character: 
                temp_var  = s[character]
                s[character] = s[counter_index]
                s[counter_index] = temp_var

            counter_index -= 1
            temp_var = ""
            
        return s