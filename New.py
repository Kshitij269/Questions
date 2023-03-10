l1=[]
l2=[]
s = "ab#c"
t = "ad#c"
for i in s:
    l1.append(i)
for i in t:
    l2.append(t)

for j in range(len(l1)):
    if l1[j]=="#":
        l1.pop(j-1)
for j in range(len(l2)):
    if l2[j]=="#":
        l2.pop(j-1)

n1="".join(l1)
n2="".join(l2)
print(True if n1==n2 else False)