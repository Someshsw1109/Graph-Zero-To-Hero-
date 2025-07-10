# Leetcode Q.No- 210 Course Schedule II

# Using Kahn's Algorithm

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Using Kahn's Algorithm
        res = []
        Count = 0
        from collections import defaultdict, deque
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)
        indegree = [0] * numCourses
        for u in range(numCourses):
            for v in adj[u]:
                indegree[v] += 1
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                res.append(i)
                Count += 1
                queue.append(i)
        while queue:
            q = queue.popleft()
            for v in adj[q]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    res.append(v)
                    Count += 1
                    queue.append(v)
        if Count == numCourses:
            return res
        else:
            return []
        

# Using DFS

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Using DFS
        # Step - 1(Make a Graph)
        from collections import defaultdict
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)
        # Step - 2(Write DFS)
        def dfs(adj, u, visited, inrecursion):
            visited[u] = True
            inrecursion[u] = True
            for v in adj[u]:
                if not visited[v] and dfs(adj, v, visited, inrecursion):
                    return True
                elif inrecursion[v] == True:
                    return True
            inrecursion[u] = False
            res.append(u)
            return False
        res = []
        visited = [False] * numCourses
        inrecursion = [False] * numCourses
        for i in range(numCourses):
            if not visited[i] and dfs(adj, i, visited, inrecursion):
                return []
        return res[::-1]