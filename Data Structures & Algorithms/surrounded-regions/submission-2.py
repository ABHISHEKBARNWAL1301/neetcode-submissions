class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            board[r][c] = "NS"
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                R = r + dr
                C = c + dc
                if  0 <= R < ROWS and 0 <= C < COLS and board[R][C] == "O":
                    dfs(R, C) 


        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1) and board[r][c] == "O":
                    dfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "NS":
                    board[r][c] = "O"


