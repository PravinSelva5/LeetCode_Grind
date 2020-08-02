class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        squared_array  = []
        
        for i in range(len(A)):
            squared_array.append(A[i] ** 2)
        
        return (sorted(squared_array))