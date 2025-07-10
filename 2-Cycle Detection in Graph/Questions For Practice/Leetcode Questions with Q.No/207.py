# Leetcode Q.No - 207 Course Schedule

# Using DFS

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        from collections import defaultdict
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
        
        def dfs(adj, u, visited, inrecursion):
            visited[u] = True
            inrecursion[u] = True
            for v in adj[u]:
                if not visited[v] and dfs(adj, v, visited, inrecursion):
                    return True
                elif inrecursion[v] == True:
                    return True
            inrecursion[u] = False
            return False
        visited = [False] * numCourses
        inrecursion = [False] * numCourses
        for i in range(numCourses):
            if not visited[i] and dfs(adj, i, visited, inrecursion):
                return False
        return True
    
# Using BFS(Kahn's Algorithm)


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Kahn's Algorithm
        Count = 0
        from collections import defaultdict, deque
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
        indegree = [0] * numCourses
        for u in range(numCourses):
            for v in adj[u]:
                indegree[v] += 1
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                Count += 1
        while queue:
            q = queue.popleft()
            for v in adj[q]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
                    Count += 1
        return Count == numCourses
