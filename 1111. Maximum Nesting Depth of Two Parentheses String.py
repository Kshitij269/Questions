seq = "(()())"

stack = []
current = 0
opening = 0
for i in seq :
    if i == "(" and opening <= 0:
        stack.append(current)
        current+=1

    elif i=="(" and opening>0:
        current+=1
        stack.append(current)
    else:
        stack.append(current)

print(stack)
