class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
         
        ROWS, COLS, max_area = len(grid), len(grid[0]), 0

        def dfs(r, c):   
            area = 1
            grid[r][c] = 0
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                R = r + dr
                C = c + dc
                if  0 <= R < ROWS and 0 <= C < COLS and grid[R][C] == 1:
                    area += dfs(R, C) 

            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
            
        return max_area
