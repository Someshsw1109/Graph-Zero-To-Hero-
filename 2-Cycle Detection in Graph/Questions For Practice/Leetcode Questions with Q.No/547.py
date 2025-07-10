# Leetcode Q.No - 547 Number of Provinces

# Solution - Using DFS-Graph Traversal

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        Count = 0
        visited = [False] * len(isConnected)
        from collections import defaultdict
        adj = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    adj[i].append(j)
        def dfs(u, adj, visited):
            visited[u] = True
            for c in adj[u]:
                if not visited[c]:
                    dfs(c, adj, visited)
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i, adj, visited)
                Count += 1
        return Count


# Without Creating Adjacency Matrix 


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Now Trying to solve this without making a graph because in question there is given an n x n matrix isConnected
        Count = 0
        visited = [False] * len(isConnected)
        # from collections import defaultdict
        # adj = defaultdict(list)
        def dfs(u, isConnected, visited):
            visited[u] = True
            for v in range(len(isConnected)):
                if not visited[v] and isConnected[u][v] == 1:
                    dfs(v, isConnected, visited)
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i, isConnected, visited)
                Count += 1
        return Count
    

# Using BFS

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        Count = 0
        visited = [False] * len(isConnected)
        from collections import defaultdict, deque
        adj = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    adj[i].append(j)
                    adj[j].append(i)
        def bfs(u, adj, visited):
            visited[u] = True
            queue = deque()
            queue.append(u)
            while queue:
                q = queue.popleft()
                for v in adj[q]:
                    if not visited[v]:
                        bfs(v, adj, visited)
        for i in range(len(isConnected)):
            if not visited[i]:
                bfs(i, adj, visited)
                Count += 1
        return Count
    
# Using BFS but this time without creating adjacency matrix

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Now Trying to solve this without making a graph because in question there is given an n x n matrix isConnected
        Count = 0
        visited = [False] * len(isConnected)
        from collections import deque
        def bfs(u, isConnected, visited):
            visited[u] = True
            queue = deque()
            queue.append(u)
            while queue:
                q = queue.popleft()
                for v in range(len(isConnected)):
                    if not visited[v] and isConnected[u][v] == 1:
                        bfs(v, isConnected, visited)
        for i in range(len(isConnected)):
            if not visited[i]:
                bfs(i, isConnected, visited)
                Count += 1
        return Count