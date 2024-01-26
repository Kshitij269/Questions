from collections import defaultdict

#[match played , match won]

di = defaultdict(lambda:[0,0])

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
for a1,a2 in matches:
    di[a1][0]+=1
    di[a1][1]+=1

    di[a2][0]+=1

print(di)

wonAll = []
lostOne = []

for i in di:
    if di[i][0] == di[i][1]:
        wonAll.append(i)
    elif di[i][0]-di[i][1] ==1 :
        lostOne.append(i)

wonAll.sort()
lostOne.sort()

return [wonAll,lostOne]