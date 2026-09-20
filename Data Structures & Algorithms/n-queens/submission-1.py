class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        prevcol = set()
        posDiag = set()
        negDiag = set()

        ans = []
        board = [["."]*n for _ in range(n)]
        
        def dfs(row):
            if row == n:
                copy = ["".join(row) for row in board]
                ans.append(copy)
                return
            
            for col in range(n):
                if col in prevcol or row+col in posDiag or row-col in negDiag:
                    continue
                    
                prevcol.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)
                board[row][col] = "Q"

                dfs(row+1)

                prevcol.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)
                board[row][col] = "."

        dfs(0)
        return ans