adj = [
 [1, 0, 1],
 [0, 1, 0],
 [1, 0, 1]
]
V = 3

from collections import defaultdict 
class Solution:
    
    def dfs (self,node,di,visited):
        visited[node]=1
        for j in di[node]:
            if (visited[j]==0):
                self.dfs(j,di,visited)    
    
    def numProvinces(self, adj, V):
        
        di = defaultdict(list)
        for i in range(V):
            for j in range(V):
                if (adj[i][j]==1 and i!=j):
                    di[i].append(j)
                    di[j].append(i)
                    
        visited = [0 for i in range(V)]
        count = 0
        for i in range(V):
            if (visited[i]==0):
                count +=1 
                self.dfs(i,di,visited)
        
        return count
