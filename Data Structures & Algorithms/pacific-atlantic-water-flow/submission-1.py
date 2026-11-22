class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
           
        ROWS, COLS = len(heights), len(heights[0])
        ans = []
        pacific, atlantic = set(), set()

        def dfs(r, c, visited):   

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                R = r + dr
                C = c + dc
                if  0 <= R < ROWS and 0 <= C < COLS and heights[R][C] >= heights[r][c] and (R,C) not in visited:
                    visited.add((R, C))
                    dfs(R, C, visited)

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pacific.add((r, c))
                    dfs(r, c, pacific)
                if r == ROWS - 1 or c == COLS - 1:
                    atlantic.add((r, c))
                    dfs(r, c, atlantic)
        
        for visit in pacific:
            if visit in atlantic:
                ans.append(visit)

        return ans
