'''
----------------------------------------
Decompress Run-Length Encoded List
----------------------------------------
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  
For each such pair, there are freq elements with value val concatenated in a sublist. 
Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.

---------------
First Attempt |  10/14/2020 21:36	Accepted	64 ms	14.5 MB	python3
---------------
'''
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        decompressed_list = []
        freq = 0
        val = 1
        
        # Loop will go through given list
        while val < len(nums):
            
            # append the value into output array based off the frequency
            for i in range(nums[freq]):
                
                decompressed_list.append(nums[val])
            
            freq += 2
            val += 2
        
        return decompressed_list

'''
---------------
Second Attempt | 10/14/2020 21:44	Accepted	64 ms	14.6 MB	python3
---------------
'''
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        freq_list = []
        val_list = []
        output_list = []    
        
        for freq in range(0,len(nums),2):
            freq_list.append(nums[freq])
        
        for val in range(1, len(nums), 2):
            val_list.append(nums[val])
            
        for i in range(len(freq_list)):
            output_list.extend([val_list[i]] * freq_list[i])
        
        return output_list

