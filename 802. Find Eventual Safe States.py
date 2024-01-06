import collections
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
di = collections.defaultdict(list)
for i in range(len(graph)):
    di[i]=graph[i]

indegree = [0 for i in range(len(graph))]
outdegree = [0 for i in range(len(graph))]

for i in di :
    outdegree[i] = len(di[i])
    for j in di[i]:
        indegree[j]+=1

ans = []

def check(indegree,outdegree,ans):
    if len(set(outdegree)) == 1:
        return ans
    for i in range(outdegree):
        if outdegree[i]==0:
            ans.append(i)


print(indegree)
print(outdegree)
print(di)