from collections import defaultdict

ans = 0
di = {5: 0, 10: 0}
for i in bills:
    if i == 5:
        di[i] += 1
        ans += 1
    elif i == 10:
        if di[5] > 0:
            di[5] -= 1
            di[10] += 1
            ans += 1
    else:
        if (di[5] > 0 and di[10] > 0):
            ans += 1
            di[5] -= 1
            di[10] -= 1
        elif (di[5] >= 3):
            di[5] -= 3
            ans += 1

if ans == len(bills):
    return True
else:
    return False

for i in bills:
    if i == 5:
        di[i] += 1
    elif i == 10 and di[5]:
        di[10] += 1
        di[5] -= 1
    elif i == 20 and ((di[5] and di[10]) or (di[5] >= 3)):
        if (di[5] > 0 and di[10] > 0):
            di[5] -= 1
            di[10] -= 1
        else:
            di[5] -= 3
    else:
        return False
return True
