'''
-----------------------------------------------------
Subtract the Product and Sum of Digits of an Integer
-----------------------------------------------------

Given an integer number n, return the difference between the product of its digits and the sum of its digits.

---------------
First Attempt |  10/14/2020 21:22	Accepted	28 ms	14.1 MB	python3
---------------

'''
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # Initialize variables
        n = str(n)
        product = 1
        total_sum = 0
        
        # Loop for sum
        for number in n:
            total_sum += int(number)
        
        # Loop for product
        for number in n:
            product *= int(number)
        
        # Difference between the two values
        return(product - total_sum)


'''
---------------
Second Attempt |  10/14/2020 21:24	Accepted	20 ms	14 MB	python3
---------------

'''

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # Initialize variables
        n = str(n)
        product = 1
        total_sum = 0
        
        # Loop for sum
        for number in n:
            total_sum += int(number)
            product *= int(number)
            
        
        # Difference between the two values
        return(product - total_sum)