#piles = [2,4,1,2,7,8]
#piles = [2,4,5]
piles = [9,8,7,6,5,1,2,3,4]

piles.sort(reverse=True)
count = 0
ans =0

count = len(piles)//3

for i in range(1,2*count,2):
    print(piles[i])
    ans += piles[i]
print(ans)