    
def MyFunct(adj, u, visited):
    from collections import deque, defaultdict
    adj = defaultdict(list)
    queue = deque()
    queue.append(u)
    visited[u] = True
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True


# ----- This is Basic BFS Code for Graph -----


# Example Question -- GFG - BFS of Graph 

class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        def BFS(adj, u, visited, res):
            from collections import deque
            queue = deque()
            queue.append(u)
            visited[u] = True
            res.append(u)
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        queue.append(v)
                        visited[v] = True
                        res.append(v)
        
        res = []
        visited = [False] * len(adj)
        BFS(adj, 0, visited, res)
        return res