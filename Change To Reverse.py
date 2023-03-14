s = "ab-cd"
left=0
right=len(s)-1
print(left,right)
l=[*s]
while left<right:
    if l[left].isalpha() and l[right].isalpha():
        l[left],l[right]=l[right],l[left]
        left+=1
        right-=1
    elif s[left].isalpha()==False:
        left+=1
    elif s[right].isalpha()==False:
        right-=1
    else:
        left+=1
        right-=1

print("".join(l))
    
