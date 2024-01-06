from collections import Counter
nums = [2,3,3,2,2,4,2,3,4]
di = dict(Counter(nums))
ans = 0
print(di)
if 1 in di.values():
    print(-1)
else:
    for i in di:
        if di[i]%3
    print(ans)
