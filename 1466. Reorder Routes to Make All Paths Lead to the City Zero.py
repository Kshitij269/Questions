from collections import defaultdict

n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
graph = defaultdict(list)

for i in range(len(connections)):
    graph[connections[i][0]].append([connections[i][1],1])
    graph[connections[i][1]].append([connections[i][0],0])

visited = set()
ans=0
def dfs(node,graph,visited):
    global ans
    if node not in visited:
        print(f"{node}->",end="")
        visited.add(node)
        for neighbour in graph[node]:
            print(neighbour)
            if neighbour[1]==1:
                ans+=1
            dfs(neighbour[0],graph,visited)

print(graph)
dfs(0,graph,visited)
print(ans)