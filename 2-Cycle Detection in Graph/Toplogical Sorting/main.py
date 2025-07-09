# Topological Sorting GFG Problem - Topological Sort


# Using DFS
class Solution:
    
    def topoSort(self, V, edges):
        # Code here
        from collections import defaultdict
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
        def dfs(adj, u, visited, Stack):
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    dfs(adj, v, visited, Stack)
            Stack.append(u)
        Stack = []
        visited = [False] * V
        for i in range(V):
            if not visited[i]:
                dfs(adj, i, visited, Stack)
        res = []
        while Stack:
            res.append(Stack.pop())
        return res