# In this file we will learn about how to create/make a graph

# Reference - Q.No - 207 Leetcode Course Schedule, I'm not going to solve this question right now, just implementing adjacency list...


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # we will make a graph here 
        from collections import defaultdict
        adj = defaultdict(list)

        for graph in prerequisites:
            v = graph[1]
            u = graph[0]

            adj[u].append(v)
        return solve(adj)