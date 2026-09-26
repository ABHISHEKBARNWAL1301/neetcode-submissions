class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:


        def dfs(row, col):
            if 0 <=row < ROWS and 0 <= col < COLS and obstacleGrid[row][col] == 0:
                if row == ROWS-1 and col == COLS-1:
                        return 1

                if (row, col) in memo:
                    return memo[(row, col)] 
                memo[(row, col)] = dfs(row+1, col) + dfs(row, col+1)
            else:
                memo[(row, col)] = 0
            
            return memo[(row, col)] 
        
        memo = {}
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        return dfs(0, 0)