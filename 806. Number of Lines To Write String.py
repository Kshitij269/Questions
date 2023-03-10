widths=[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "abcdefghijklmnopqrstuvwxyz"
l=[]
n=[]
sum1=0
def rec():
    for i in range(len(s)):
    if sum1>=100:
        l.append(s[0:i])
        n.append(sum1)
        break
    else:
        sum1+=widths[i]

while len(s)>0:
    s=s[i:len(s)]
    print(s)
    
    
print(l)
print(n)
