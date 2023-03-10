s="RLRRRLLRLL"
balance=0
answer=0
for i in s:
    if i=="L" :
        balance +=1
    else:
        balance-=1
    if balance==0:
        answer+=1
print(answer)
