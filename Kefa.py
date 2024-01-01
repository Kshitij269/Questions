import collections
global k,ans

n,k=map(int,input().split())
cats = [int(x) for x in input().split()]

def dfs(sv,m):
	visited[sv]=1
    if m>k:
        return 
    flag = 1
    for i in adj_list[sv]:
        if (visited[i]==0):
            flag=0
            dfs(i,m*cats[i]+cats[i])
    if (flag):
        ans+=1
    
adj_list = collections.defaultdict(list)
for i in range(n-1):
    x,y = [int(z)-1 for z in input().split()]
    adj_list[x].append(y)
    adj_list[y].append(x)

visited = [0]*n

dfs(0,cats[0])