from heapq import heapify,heappop,heappush
s = "cccaaa"
nums=[]

for i in s :
    heappush(nums,i)

for i in range(len(s)) :
    print(heappop(nums))

for i,j in enumerate(s):
    print(i,j)
