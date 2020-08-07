'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Notes
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Unfortunately had to reference the solutions for this question
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        #Pointers for nums1 & nums2
        p1 = m - 1
        p2 = n - 1
        
        #Pointer for nums1
        p = m + n - 1
        
        while p1 >= 0  and p2 >= 0:
            
            if nums2[p2] > nums1[p1]:
                nums1[p] = nums2[p2]
                p2 -= 1
            
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            
            p -= 1
        
        # If there are still
        nums1[:p2 + 1] = nums2[:p2 + 1] 
