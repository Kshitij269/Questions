from collections import deque
class Solution:
    def topoSort(self, V, adj):
        indegree = [0 for i in range(V)]
        for i in range(V):
            for it in adj[i]:
                indegree[it] += 1
        q = deque()
        for i in range(V):
            if (indegree[i] == 0):
                q.append(i)
        top = []
        while (q):
            node = q[-1]
            q.pop()
            top.append(node)
            for i in adj[node]:
                indegree[i] -= 1
                if (indegree[i] == 0):
                    q.append(i)
        return top