from heapq import heapify,heappop,heappush
score = [5,4,3,2,1]
nums=[]
medals = ["Gold Medal","Silver Medal","Bronze Medal"]
for i in score :
    heappush(nums,-i)


l2=enumerate(score)
counter = 0
for i in range(len(score)):
    l=abs(heappop(nums))
    if counter < 3:
        score[score.index(l)]=medals[counter]
    else :
        score[score.index(l)]=counter+1
    counter +=1
print(score)
