class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Initialize a dictionary that will contain the # of occurences
        occurences_dictionary = {}
        
        #Loop through the given array and append occurences to dictonary
        
        for number in nums:
            
            if number in occurences_dictionary:
                occurences_dictionary[number] += 1
            
            else:
                occurences_dictionary[number] = 1
        
        
        for key, val in occurences_dictionary.items():
            if (val >= len(nums)/2):
                return key

'''
COULD'VE SORTED THE LIST FIRST AND THEN RETURNED THE INTEGER IN THE N/2 INDEX
'''