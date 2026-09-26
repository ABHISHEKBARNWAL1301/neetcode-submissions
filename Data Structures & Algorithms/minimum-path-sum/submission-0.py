class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        

        # def dfs(row, col):
        #     if 0 <=row < ROWS and 0 <= col < COLS:
        #         if row == ROWS-1 and col == COLS-1:
        #                 return grid[row][col]

        #         return  grid[row][col] + min(dfs(row+1, col), dfs(row, col+1))
            
        #     return float(math.inf)
        
        # ROWS, COLS = len(grid), len(grid[0])
        # return dfs(0, 0)
            
        
        ROWS, COLS = len(grid), len(grid[0])

        dp =[[0]*(COLS) for _ in range(ROWS)]

        dp[0][0]= grid[0][0]
        
        for i in range(1,ROWS):
            dp[i][0]=grid[i][0]+dp[i-1][0]
        for j in range(1,COLS):
            dp[0][j]=grid[0][j]+ dp[0][j-1]

        for i in range(1,ROWS):
            for j in range(1,COLS):
                dp[i][j]= grid[i][j] + min(dp[i-1][j],dp[i][j-1])

        return dp[ROWS-1][COLS-1]