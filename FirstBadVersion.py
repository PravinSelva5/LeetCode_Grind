# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

===============
    RESULTS
===============
Runtime: 28 ms, faster than 68.57% of Python3 online submissions for First Bad Version.
Memory Usage: 14 MB, less than 78.57% of Python3 online submissions for First Bad Version.
'''
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start_ptr = 1
        end_ptr = n
        
        while (start_ptr < end_ptr):
            midpoint = (start_ptr + end_ptr) // 2
            
            # If midpoint is a bad version, save value and set end pointer to midpoint
            if isBadVersion(midpoint):
                end_ptr = midpoint
            # If midpoint isn't a bad version, set start pointer to one index after the current midpoint
            else:
                start_ptr  = midpoint + 1
            
            midpoint = (start_ptr + end_ptr) // 2
        
        return end_ptr