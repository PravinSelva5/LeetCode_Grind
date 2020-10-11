'''
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
      
        # J string is unique
        
        # Initialize a counter variable
        number_of_jewels = 0
        
        # Loop through the stones string
        for jewels in S:
                
                # Compare if the current letter is present in J
                if jewels in J:
                    
                    # If it is, increment number_of_jewels by one
                    number_of_jewels += 1
            
                # If not, continue through the loop
                else:
                    continue
        
        
        # Return number_of_jewels
        return number_of_jewels

10/10/2020 23:17	Accepted	44 ms	14 MB	python3
'''
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        '''J string is unique '''
        
        
        number_of_occurences = {}
        counter = 0
        
        # Count the number of each stone you have
        for stone in S:
            
            if stone in number_of_occurences :
                
                number_of_occurences[stone] += 1
            
            else:
                number_of_occurences[stone] = 1
        
        
        for jewel in J:
            
            if jewel in number_of_occurences:
                
                counter += number_of_occurences[jewel]
            
            else:
                continue
        
        return counter

# 10/10/2020 23:23	Accepted	24 ms	14.1 MB	python3