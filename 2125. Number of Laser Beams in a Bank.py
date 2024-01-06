l = ["000","111","000"]
n=[]
for i in l:
    if int(i) != 0:
        n.append(i)
ans=0
for i in range(len(n)-1):
    a=n[i].count("1")
    b=n[i+1].count("1")
    ans= ans+a*b
print(ans)