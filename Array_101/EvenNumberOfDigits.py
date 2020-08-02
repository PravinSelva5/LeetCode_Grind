class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = total_digits = 0
        
        for i in range(len(nums)):
            number = nums[i]
            # this while loop will check how many digits are present in each number in the provided list
            while (number > 0):
                number = number // 10
                count += 1
                
        # will check if count value is an even number 
            if (count % 2 == 0):
                total_digits += 1
           
        # Set count to 0 for the next number doesn't add on to the previous count
            count = 0
            
        return total_digits