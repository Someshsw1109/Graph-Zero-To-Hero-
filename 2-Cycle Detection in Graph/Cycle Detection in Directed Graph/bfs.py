# Directed Graph using BFS

# Using Kahn's Algorithm


class Solution:
    def isCycle(self, V, edges):
        # code here
        Count = 0
        from collections import defaultdict
        adj = defaultdict(list)
        # visited = [False] * V
        # make a graph
        for u, v in edges:
            adj[u].append(v)
        indegree = [0] * V
        for u in range(V):
            for v in adj[u]:
                indegree[v] += 1
        from collections import deque
        queue = deque()
        for i in range(V):
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
        
        if Count == V:
            return False
        else:
            return True
        