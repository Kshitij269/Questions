costs=[7,3,3,6,6,6,10,5,9,2]
coin=56
m=sorted(costs)
c=0
if m[0]>coin:
    print(0)
else:
    for i in range(len(costs)):
        if costs[i]<=coin:
           coin-=costs[i]
           c+=1
        else:
            break
print(c)
