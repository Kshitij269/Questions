digits = [1, 2, 0,0]
l=""
k=34
m=[]
for i in digits:
    l+=str(i)
n=str(int(l)+k)
for y in n:
    m.append(int(y))
print(m)