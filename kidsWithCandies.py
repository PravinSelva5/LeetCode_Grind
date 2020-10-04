class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Assign the max number to a variable 
        
        #max_candies = max(candies)
        greatest = 0
        candy_pointer = 0
        
        for i in candies:
            if i >= greatest:
                greatest = i
    
        # Loop through each kids number of candies
        for candy in candies:
            # Compare the maximum number of candies each kid can have with the max_candies
            if candy + extraCandies >= greatest:
                candies[candy_pointer] = True 
                
            else:
                candies[candy_pointer] = False
            
            candy_pointer += 1
        
        return candies
                