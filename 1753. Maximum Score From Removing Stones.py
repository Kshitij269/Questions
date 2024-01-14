a=1
b=8
c=8

count = 0
l = [a, b, c]
l.sort(reverse=True)
print(l)
while len(set(l)) > 1 or 0 not in set(l):
    if (l[0]>0 and l[1]>0):
        l[0] -= 1
        l[1] -= 1
        print(l)
        l.sort(reverse=True)
        count += 1

print(count)