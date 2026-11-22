class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        numFresh, timer = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    numFresh += 1
        
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    R = r + dr
                    C = c + dc
                    if  0 <= R < ROWS and 0 <= C < COLS and grid[R][C] == 1:
                        grid[R][C] = 2
                        numFresh -= 1
                        queue.append((R, C))
            if queue:
                timer += 1


        return timer if numFresh == 0 else -1



