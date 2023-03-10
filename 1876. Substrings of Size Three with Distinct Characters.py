s="aababcabc"
l=[]
c=0
for i in range(0,len(s)-2):
    l.append(s[i:i+3])
for i in l:
    if len(set(i))==3:
        c+=1
print(c)



