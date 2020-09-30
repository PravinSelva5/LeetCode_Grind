'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

RESULTS
---------
09/29/2020 22:49	Accepted	76 ms	14.2 MB	python3
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Determine the smallest length array of the two
        # Loop through small area and see if the current val is in the second array
        
        intersection_values = []
        if len(nums1) <= len(nums2):
            smallest_arr = nums1
            largest_arr = nums2
        else:
            smallest_arr = nums2
            largest_arr = nums1
        
        
        for i in smallest_arr:
            
            if (i not in intersection_values) and (i in largest_arr):
                intersection_values.append(i)
        
        return intersection_values

'''
----------------------------------------------------------------------------
ATTEMPT TWO USING SETS METHOD TO GET DISTINCT VALUES BASED OFF THE QUESTION
----------------------------------------------------------------------------

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        list1 = set(nums1)
        list2 = set(nums2)
        
        return list1 & list2


RESULTS
---------
09/29/2020 22:58	Accepted	44 ms	14.3 MB	python3
---------
'''

