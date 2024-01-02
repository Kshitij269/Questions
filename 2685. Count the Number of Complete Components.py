from collections import defaultdict
def dfs(node, di, visited):
    visited[node] = 1
    for j in di[node]:
        if (visited[j] == 0):
            dfs(j, di, visited)

n = 6
edges = [[0,1],[0,2],[1,2],[3,4]]
di = defaultdict(list)

for edge in edges:
    di[edge[0]].append(edge[1])
    di[edge[1]].append(edge[0])

print(di)
visited = [0 for i in range(n)]
count = 0

for i in range(n):
    if (visited[i] == 0):
        count += 1
        dfs(i, di, visited)

print(count)
