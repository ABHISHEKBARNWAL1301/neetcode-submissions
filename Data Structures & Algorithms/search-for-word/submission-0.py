class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        def dfs(i, j, string):
            char = board[i][j]
            board[i][j] = "#"
            if len(string) == len(word):
                board[i][j] = char
                return string == word 
            
            dirn = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            res = False
            for di in dirn:
                I = i + di[0]
                J = j + di[1]

                if 0 <= I < rows and 0 <=J < cols and board[I][J] != "#":
                    res = res or dfs(I, J, string+board[I][J])
            
            board[i][j] = char
            return res


        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    res = dfs(i, j, word[0])
                    if res == True:
                        return res

        return False
