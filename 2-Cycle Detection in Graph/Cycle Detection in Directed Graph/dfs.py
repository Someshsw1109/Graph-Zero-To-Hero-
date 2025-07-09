# GFG Problem - Detect Cycle in a Directed Graph


class Solution:
    def isCycle(self, V, edges):
        # code here
        from collections import defaultdict
        adj = defaultdict(list)
        for u, v in edges:
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
        
        visited = [False] * V
        inrecursion = [False] * V
        for i in range(V):
            if not visited[i] and dfs(adj, i, visited, inrecursion):
                return True
        return False