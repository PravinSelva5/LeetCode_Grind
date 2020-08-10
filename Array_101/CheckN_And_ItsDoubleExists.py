'''
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
'''

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashTable=set()
        for i in range(len(arr)):
            if ( arr[i]*2 in hashTable or arr[i]/2 in hashTable):
                return True
            hashTable.add(arr[i])
        return False