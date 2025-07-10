# GFG Problem Link - https://www.geeksforgeeks.org/problems/bipartite-graph

# Using DFS

class Solution:
    def isBipartite(self, V, edges):
        # code here
        from collections import defaultdict
        adj = defaultdict(list)
        for u, v in edges:
            adj[v].append(u)
            adj[u].append(v)
        color = [-1] * V
        def CheckBiPartiteDFS(adj, u, color, currentcolor):
            color[u] = currentcolor
            for v in adj[u]:
                if color[v] == color[u]:
                    return False
                if color[v] == -1:
                    ColorOfV = 1 - currentcolor
                    if CheckBiPartiteDFS(adj, v, color, ColorOfV) == False:
                        return False
            return True
        for i in range(V):
            if color[i] == -1:
                if CheckBiPartiteDFS(adj, i, color, 1) == False:
                    return False
        return True