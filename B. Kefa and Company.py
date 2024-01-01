a,b = map(int,input().split())
main=[]
for i in range(a):
    l1,l2 = map(int,input().split())
    l=[l1,l2]
    main.append(l)

l=sorted(main)

low = 0
high = a-1

flag = 0

while low<=high:
    mid = (high+low)//2
    if l[mid][0]==b:
        low = mid
        break
    elif l[mid][0]<b:
        low=mid+1
    else:
        high=mid-1

ans = 0
for i in range(low):
    ans +=l[i][1]
        
print(ans)
