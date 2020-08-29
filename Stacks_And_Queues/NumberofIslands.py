"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
"""
class Solution:
    import collections
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows = len(grid)
        columns = len(grid[0])
        visited_cells = set()
        islands = 0
        
        def bfs(r,c):
            queue = collections.deque()
            visited_cells.add((r,c))
            queue.append((r,c))
            
            # While queue is not empty
            
            while queue:
                row, col = queue.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                
                for dx, dy in directions:
                    r,c = row + dx, col + dy
                    if ((r) in range(rows) and (c) in range(columns) and grid[r][c] == "1" and (r, c) not in visited_cells):
                        queue.append((r, c))
                        visited_cells.add((r, c))
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r,c) not in visited_cells:
                    bfs(r,c)
                    islands += 1
        return islands