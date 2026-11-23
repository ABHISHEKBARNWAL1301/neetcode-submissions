class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for (u, v, w) in times:
            graph[u].append((v, w))

        dist = {k: 0}
        h = [(0, k)]

        while h:
            d, u = heapq.heappop(h)

            for v, w in graph[u]:
                nd = d + w
                if dist.get(v, float('inf')) > nd:
                    dist[v] = nd
                    heapq.heappush(h, (nd, v))

        if len(dist) != n:
            return -1 
        
        return max(dist.values())

