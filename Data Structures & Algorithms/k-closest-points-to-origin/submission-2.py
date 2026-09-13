class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        closest = []
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            if len(closest) == k:
                if distance < -closest[0][0]:
                    heapq.heapreplace(closest, (-distance, point))
            else:
                heapq.heappush(closest, (-distance, point))

        return [closest[i][1] for i in range(k)]
