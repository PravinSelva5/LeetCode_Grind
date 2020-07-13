''' 
#----------------------------------------------------------------------#
#       FIRST ATTEMPT - DID NOT WORK FOR SOME REASON, WOULDN'T ITERATE.
#----------------------------------------------------------------------#

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_dict = {i:5 for i in list}
        if (len(List) > len(new_dict)):
            print(True)
        else:
            print(False)


#----------------------------------------------------------------------#
#               RUNTIME: 236ms & MEMORY USAGE: 19MB
#----------------------------------------------------------------------#
'''
 class Solution:
        def containsDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        nums.sort()
        bool = False
        for i in range(length):
            if (length == 1):
                bool = False
                break
            elif (nums[i] == nums[i+1]):
                bool = True
                break
            elif (i+1 == length-1):
                bool = False
                break
        return bool