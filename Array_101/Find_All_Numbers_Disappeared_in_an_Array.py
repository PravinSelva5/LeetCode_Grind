'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Solution only got 30/34 Time Exceeded Limit when the input was too large
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums) + 1
        missing_values = []
        
        for i in range(1,length):
            
            if i not in nums:
                missing_values.append(i)
        
        return missing_values
'''

'''
Solution Worked
O(n) time complexity
The other solution was O(n**2) which is why when the input was too large, it took too much time to finish
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        missing_values = []
        
        for i in range(length):
            j = abs(nums[i]) - 1
            nums[j] = abs(nums[j]) * -1
            
        for num in range(length):
            if nums[num] > 0 :
                missing_values.append(num+1)
        
        return missing_values
