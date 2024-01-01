a,b,c,d,=map(int,input().split())
string = input()
ans = 0
for i in string :
    if i=='1':
        ans +=a
    elif i=='2':
        ans +=b
    elif i=='3':
        ans +=c
    elif i=='4':
        ans +=d
print(ans)
