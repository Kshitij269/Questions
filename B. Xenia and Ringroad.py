from collections import defaultdict

n,target = map(int,input().split())
l=list(map(int,input().split()))
arr = []

adj_list = defaultdict(list)

visited=set()
def createNode(l):
    for i in range(n-1):
        x=i+1
        y=l[i]+i+1
        arr.append([x,y])
        adj_list[x].append(y)

def dfs(visited, adj_list, node):  #function for dfs 
    if node not in visited:
        arr.append(node)
        visited.add(node)
        for neighbour in adj_list[node]:
            dfs(visited, adj_list, neighbour)

createNode(l)
dfs(visited, adj_list, 1)       
if target in arr:
    print("YES")
else :
    print("NO")
