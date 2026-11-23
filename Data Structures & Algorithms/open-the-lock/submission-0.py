class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        queue = deque(["0000"])
        if "0000" in deadends:
            return -1
            
        res = 0
        visited = set(deadends)
        while queue:
            for _ in range(len(queue)):
                u = queue.popleft()
                for posn in range(4):
                    for move in (-1, 1):
                        new_digit = (int(u[posn]) + move) % 10
                        code = u[:posn] + str(new_digit) + u[posn+1:]
                        if code == target:
                            return res + 1
                        if code not in visited:
                            queue.append(code)
                            visited.add(code)
            if queue:
                res += 1
        
        return -1



