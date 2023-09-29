class Solution:
    def dfs(self, node, visited, stack, adj):
        visited[node] = 1
        for i in adj[node]:
            if (visited[i] == 0):
                self.dfs(i, visited, stack, adj)
        stack.append(node)

    def topoSort(self, V, adj):
        visited = [0 for i in range(V)]
        stack = []
        for i in range(V):
            if (visited[i] == 0):
                self.dfs(i, visited, stack, adj)

        ans = []
        while (stack):
            ans.append(stack[-1])
            stack.pop()

        return ans