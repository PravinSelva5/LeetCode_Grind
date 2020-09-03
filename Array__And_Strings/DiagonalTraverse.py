"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

NEEDED SOLUTION FOR THIS QUESTION
"""

class Solution:
    
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # Check if the given array is empty
        if not matrix or not matrix[0]:
            return []
        
        result_array, temp_array = [] , []
        M_row = len(matrix)
        N_column = len(matrix[0])
        
        # Subtract one so you don't double count the middle diagonal
        for i in range(N_column + M_row - 1):
            
            #clear temp array every time you read through a new diagonal
            temp_array.clear()
            
            # Trying to figure out when the start of the diagonal begins
            r = 0 if i < N_column else i - N_column + 1
            c = i if i < N_column else N_column - 1
            
            # We will iterate through all the elements in current diagonal
            while r < M_row and c > -1:
                temp_array.append(matrix[r][c])
                r += 1
                c -= 1
            
            # Now we need to check if the current diagonal is odd or even. If even, elements needs to be reversed
            
            if i % 2 == 0:
                result_array.extend(temp_array[::-1])
            else:
                result_array.extend(temp_array)
        
        return result_array  