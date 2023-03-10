from collections import Counter
import math
tasks = [2,2,3,3,2,4,4,4,4,4]
l=dict(Counter(tasks))
print(l)
def mint(tasks):
    ans=0
    for i in l:
        if l[i]==1:
            return -1
        elif l[i]==len(tasks):
            return(math.ceil(min(l[i]/2,l[i]/3)))
        else:
            ans+=math.ceil(min(l[i]/2,l[i]/3))
            print(ans)

    return(ans)

l=mint(tasks)
print(l)
