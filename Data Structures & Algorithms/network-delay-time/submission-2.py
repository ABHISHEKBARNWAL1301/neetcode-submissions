class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        # # 1. Dijkstra's 
        # graph = defaultdict(list)
        # for (u, v, w) in times:
        #     graph[u].append((v, w))

        # dist = {k: 0}
        # h = [(0, k)]

        # while h:
        #     d, u = heapq.heappop(h)

        #     for v, w in graph[u]:
        #         nd = d + w
        #         if dist.get(v, float('inf')) > nd:
        #             dist[v] = nd
        #             heapq.heappush(h, (nd, v))

        # if len(dist) != n:
        #     return -1 
        
        # return max(dist.values())




        # # 2. Floyd Warshall's Algo 

        # dist = [[float('inf')] * n for _ in range(n)]
        # for u, v, w in times: dist[u-1][v-1] = w
        # for i in range(n): dist[i][i] = 0

        # for mid in range(n):
        #     for i in range(n):
        #         for j in range(n):
        #             if dist[i][mid] + dist[mid][j] < dist[i][j]:
        #                 dist[i][j] = dist[i][mid]+ dist[mid][j]
         
        # ans = max(dist[k - 1])

        # if ans == float('inf'):
        #     return -1
        
        # return ans

 
        # 3. Belleman Ford Algorithm
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = [float('inf')] * n
        dist[k-1] = 0

        for _ in range(n - 1):
            for u, v, w in times:
                if dist[v-1] > dist[u-1] + w:
                    dist[v-1] = dist[u-1] + w

        ans = max(dist)
        if ans == float("inf"):
            return -1

        return ans



       