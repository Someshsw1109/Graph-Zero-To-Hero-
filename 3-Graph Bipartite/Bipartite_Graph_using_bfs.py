# Leetcode Q.No- 785 Is Graph Bipartite?

from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Using BFS
        n = len(graph)
        color = [-1] * n
        def CheckBiPartiteBFS(graph, u, color, currentcolor):
            from collections import deque
            queue = deque()
            queue.append(u)
            color[u] = currentcolor
            while queue:
                q = queue.popleft()
                for v in graph[q]:
                    if color[v] == color[q]:
                        return False
                    elif color[v] == -1:
                        color[v] = 1 - color[q]
                        queue.append(v)
            return True
        for i in range(len(graph)):
            if color[i] == -1:
                if CheckBiPartiteBFS(graph, i, color, 1) == False:
                    return False
        return True
