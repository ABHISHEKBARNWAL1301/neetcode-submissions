class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
    
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        fresh, timer = 0, 0
        directions = [(0,1), (0,-1),(1,0),(-1,0)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1 

        while queue:
            size = len(queue)
            for i in range(size):
                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] == 1:
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = 2
                        fresh -= 1
            
            if queue:
                timer += 1

        return -1 if fresh else timer 
            



