s="010"
l=[*s]
print(l)
l.sort(reverse=True)
l.pop(0)
l.append('1')
print("".join(l))

