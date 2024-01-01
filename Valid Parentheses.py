s="(){}}{"
stack = []
l=[*s]
stack.append(s[0])
for i in range(1,len(l)):
    try :
        if stack[-1]=="(" and s[i]==")":
            stack.pop()
        elif stack[-1]=="{" and s[i]=="}":
            stack.pop()
        elif stack[-1]=="[" and s[i]=="]":
            stack.pop()
        else:
            stack.append(s[i])
    except IndexError :
        stack.append(s[i])
if len(stack)==0:
    print(True,stack)
else:
    print(False,stack)
