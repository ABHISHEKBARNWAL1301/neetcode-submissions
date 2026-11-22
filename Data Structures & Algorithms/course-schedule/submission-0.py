class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph  = defaultdict(list)
        indegree = [0]*numCourses

        for edges in prerequisites:
            graph[edges[1]].append(edges[0])
            indegree[edges[0]] += 1
        
        queue = deque()
        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)
        
        courses = []
        while queue:
            u = queue.popleft()
            courses.append(u)

            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        return len(courses) == numCourses




        
        