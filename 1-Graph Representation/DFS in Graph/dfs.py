from collections import defaultdict
adj = defaultdict(list)

def dfs(adj, u, visited):
    if visited[u] == True: # This states that we already visited this...
        return
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs(adj, v, visited) # This states that if it is not visited then we need to do a traversal to visit it...



# One Example - GFG - DFS of Graph

# Solution:

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        # code here
        def DFS(adj, u, visited, res):
            if visited[u] == True:
                return
            visited[u] = True
            res.append(u)
            for v in adj[u]:
                if not visited[v]:
                    DFS(adj, v, visited, res)
        res = []
        visited = [False] * len(adj)
        DFS(adj, 0, visited, res)
        return res