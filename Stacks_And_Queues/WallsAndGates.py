'''
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
'''

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        # Check if the rooms are empty
        if rooms == None or rooms == []:
            return
        
        # Get the rows and columns of the rooms list
        rows = len(rooms)
        columns = len(rooms[0])
        queue = []
        empty = 2147483647 
        grid = [[1,0], [0,1], [-1,0], [0,-1]]
        
        # find coordinates of where gates are present
        
        for row in range(rows):
            for column in range(columns):
                if rooms[row][column] == 0:
                    queue.append([row,column])
                    
        # BFS algorithm
        
        while queue:
            # Pop out coordinates of first gate
            r, c = queue.pop(0)
            
            
            for x,y in grid:
                # Check around the gate if there any empty cells
                delta_x = x + r
                delta_y = y + c
                
                # Avoiding going out of bounds
                if delta_x < 0 or delta_y < 0 or delta_x >= rows or delta_y >= columns:
                    continue
                
                # Replace empty room with distance value and add its position to queue to be checked
                if rooms[delta_x][delta_y] == empty:
                    rooms[delta_x][delta_y] = rooms[r][c] + 1
                    queue.append([delta_x,delta_y])