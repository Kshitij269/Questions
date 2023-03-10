l=[]
for i in range(int(input())):
    a=list(map(int,input().split()))
    l.append(a)
n=sorted(l,key=lambda l : l[0])

end=n[0][1]
watch=1

for i in range(len(n)):
    if n[i][0]>=end:
        watch+=1
        end=n[i][1]

print(watch)
    
