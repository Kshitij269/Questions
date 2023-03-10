num=9669
l=[i for i in str(num)]
n=[]
print(l)
for i in range(len(l)):
    f=l.copy()
    if f[i]=='9':
        f[i]='6'
    else:
        f[i]='9'

    n.append("".join(f)) 
        
print(max(n))
