from collections import defaultdict

V = 5
E = 5

adj = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
di = defaultdict(list)
for i in range(V):
    di[i]=adj[i]

print(di)
