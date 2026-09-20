class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        ans = []
        board = [["."]*n for _ in range(n)]
        
        def isSafe(r, c):
            row = r - 1
            while row >= 0:
                if board[row][c] == "Q":
                    return False
                row -= 1

            row, col = r - 1, c - 1
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1

            row, col = r - 1, c + 1
            while row >= 0 and col < len(board):
                if board[row][col] == "Q":
                    return False
                row -= 1
                col += 1
            return True

        def dfs(row):
            if row == n:
                copy = ["".join(row) for row in board]
                ans.append(copy)
                return
            
            for col in range(n):
                if isSafe(row, col):
                    board[row][col] = "Q"
                    dfs(row+1)
                    board[row][col] = "."

        dfs(0)
        return ans