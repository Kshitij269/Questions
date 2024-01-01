import collections
from collections import defaultdict

adj_list=defaultdict(list)

n,m = map(int,input().split())
for i in range(m):
  a,b = map(int,input().split())
  adj_list[a].append(b)
  adj_list[b].append(a)
l=[]
count=0
ans = [False]*m
def bfs(graph, root,l,ans):
    global count
    f=[]
    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:
       vertex = queue.popleft()
       f.append(vertex)
       for neighbour in graph[vertex]:
         if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)
    e = sorted(f)
    if e not in l:
        l.append(e)
    

for s in range(1,n+1):
    bfs(adj_list,s,l,ans)
print(len(l)-1)
