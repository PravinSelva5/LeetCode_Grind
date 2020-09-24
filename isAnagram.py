class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Loop through the first string
            Append each letter to a dictonary
        
        Loop through the second string
            Append each letter to second dictonary
            
        Loop through first dictonary:
            compare key value with other dictionary
                increment a variable by the key value
        
        If both dictionaries are the same
            return True
        Else
            return False
        """

        
        first_dict = {}
        second_dict = {}
        counter = 0 
        
        for letter in s:
            if letter  in first_dict:
                first_dict[letter] += 1
            else:
                first_dict[letter] = 1
        
        for letter_2 in t:
            if letter_2  in second_dict:
                second_dict[letter_2] += 1
            else:
                second_dict[letter_2] = 1
                
        
        if first_dict == second_dict:
            return True
        else:
            return False
        
                