# GFG Problem Link - https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
# problem - Detect Cycle in an Undirected Graph


class Solution:
        def isCycle(self, V, edges):
            #Code here
            from collections import defaultdict
            adj = defaultdict(list)
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            def dfs(adj, u, visited, parent):
                visited[u] = True
                for v in adj[u]:
                    if v == parent:
                        continue
                    if visited[v] == True:
                        return True
                    if dfs(adj, v, visited, u) == True:
                        return True
                return False
            visited = [False] * V
            for i in range(V):
                if not visited[i] and dfs(adj, i, visited, -1):
                    return True
            return False