num = 687
s=str(num)
l=[*s]
l.sort()
num1=""
num2=""
for i in range(0,len(l),2):
    num1+=l[i]
    try:
        num2+=l[i+1]
    except IndexError:
        pass
print(int(num1)+int(num2))
