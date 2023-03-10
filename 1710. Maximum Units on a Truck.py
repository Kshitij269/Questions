boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
answer=0
l=sorted(boxTypes, key=lambda boxTypes: boxTypes[1],reverse=True)
print(l)
for i in l:
    if truckSize-i[0]>=0:
        truckSize-=i[0]
        answer+= (i[0]*i[1])
        print(truckSize , answer ,i[0] ,i[1])
    else:
        answer+= (truckSize*i[1])
        print(truckSize , answer ,i[0] ,i[1])
        break
print(answer)
