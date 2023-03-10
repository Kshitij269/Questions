l=[]
s="leet**cod*e"
l.append(s[0])
for i in s[1:len(s)]:
    try:
        if i=="*":
            l.pop()
        else:
            l.append(i)
    except IndexError:
        l.append(i)
print(''.join(l))
