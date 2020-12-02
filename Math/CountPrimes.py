'''
------------------------------
        Count Primes
------------------------------
Count the number of prime numbers less than a non-negative number, n.

Runtime: 364 ms, faster than 84.25% of Python3 online submissions for Count Primes.
Memory Usage: 25.7 MB, less than 53.34% of Python3 online submissions for Count Primes.

Use Sieve of Eratosthenes:  
        - define a boolean array of size n & set elements to True except 0 and 1
'''
import math

class Solution:
    def countPrimes(self, n: int) -> int:
        
        # If input number is less than 2
        if n < 2:
            return 0
        
        # Create boolean array
        boolean_array = [True] * n
        boolean_array[0] = boolean_array[1] = False
        
        for i in range(2, int(math.ceil(math.sqrt(n)))):
            
            if ( boolean_array[i] ):
                for multiples_of_i in range(i*i, n, i):
                    boolean_array[multiples_of_i] = False
        
        return sum(boolean_array)

s = Solution()
answer = s.countPrimes(12)
print(answer)