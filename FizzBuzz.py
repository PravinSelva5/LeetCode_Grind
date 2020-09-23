class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        '''
        - Initialize an output list
        - Run a for-loop for the length of n 
            
            - If number % 5 == 0 and number % 3 == 0
                - append FizzBuzz to list
            - Else if number % 5 == 0 
                - append Buzz to list
            - Else if number % 3 == 0
                - append Fizz to list
            - Else
                - append integer value
        - return list
        '''
        
        output_array = []
        
        for number in range(1,n+1):
            
            if number % 3 == 0 and number % 5 == 0:
                output_array.append('FizzBuzz')
            
            elif number % 5 == 0:
                output_array.append("Buzz")
                
            elif number % 3 == 0:
                output_array.append("Fizz")
            
            else:
                output_array.append(str(number))
        
        return output_array