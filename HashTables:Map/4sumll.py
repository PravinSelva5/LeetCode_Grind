'''
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.


Time Complexity: O(N^2)
Space Complexity: O(N)
---------
RESULTS 
---------
Runtime: 304 ms, faster than 44.04% of Python3 online submissions for 4Sum II.
Memory Usage: 39 MB, less than 41.61% of Python3 online submissions for 4Sum II.

'''

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        
        hashmap = {}
        output = 0
        # Loop through array A
        # Find the sum between an integer in A and every value in B
        # Increment the number of occurences of the sum in a map
        for numA in A:
            for numB in B:
                temp = numA + numB
                hashmap[temp] = hashmap.get(temp, 0) + 1
        
        print(hashmap)
        # Loop through Array B 
        # Find the sum of an integer in C and every value in D
        # Compare it with values in hashmap
        # If the values match, increment output
        for numC in C:
            for numD in D:
                temp2 =  -1 * (numC + numD)
                
                if temp2 in hashmap:
                    output += hashmap[temp2]
          
        return output
        
        