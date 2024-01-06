s = "seven"

low = 0
high = len(s)-1
s=[*s]
while low<=high:
    if s[low]!=s[high]:
        if s[low]>s[high]:
            s[low]=s[high]
        else:
            s[high]=s[low]
    low+=1
    high-=1
print(''.join(s))