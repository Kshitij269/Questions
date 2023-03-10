prices=[10,1,1,6]
l=len(prices)
ans=[]
for i in range(l):
    for j in range(i+1,l):
         if i!=j and prices[i]>=prices[j]:
             max_index=j
             break    
    n=prices[i]-prices[j]
    if n >= 0:
        ans.append(n)
    else:
        ans.append(prices[i])

ans[-1]=prices[-1]
print(ans)
