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
            def bfs(adj, u, visited):
                from collections import deque
                queue = deque()
                queue.append((u, -1))
                visited[u] = True
                while queue:
                    q = queue.popleft()
                    first = q[0]
                    second = q[1]
                    for v in adj[first]:
                        if visited[v] == False:
                            visited[v] = True
                            queue.append((v, first))
                        elif v != second:
                            return True
                return False
                
            visited = [False] * V
            for i in range(V):
                if not visited[i] and bfs(adj, i, visited):
                    return True
            return False