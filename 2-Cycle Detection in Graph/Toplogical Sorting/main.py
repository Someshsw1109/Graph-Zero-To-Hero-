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
    
# Using BFS

# Kahn's Algorithm

class Solution:
    
    def topoSort(self, V, edges):
        # Code here
        
        from collections import defaultdict
        # Make a Graph
        adj = defaultdict(list)
        # Directed Graph hai isilie sirf ekk side hi jaa skte 1--->2
        for u, v in edges:
            adj[u].append(v)
        
        # Write the indegree of all the edges...
        indegree = [0] * V
        for u in range(V):
            for v in adj[u]:
                indegree[v] += 1
        
        # Take a queue and fill it by adding those edges whose indegree is currently 0
        from collections import deque
        queue = deque()
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        res = []
        while queue:
            q = queue.popleft()
            res.append(q)
            for v in adj[q]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        return res
                    
        