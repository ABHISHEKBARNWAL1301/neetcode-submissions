class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
         
        ROWS, COLS, num_island = len(grid), len(grid[0]), 0

        def dfs(r, c):   
            grid[r][c] = "0"
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                R = r + dr
                C = c + dc
                if  0 <= R < ROWS and 0 <= C < COLS and grid[R][C] == "1":
                    dfs(R, C) 


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    num_island += 1
                    dfs(r, c)
            
        return num_island
