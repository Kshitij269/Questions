current = "11:00"
correct = "11:01"

l = current.split(":")
m = correct.split(":")

current_min = int(l[0]) * 60 + int(l[1])
correct_min = int(m[0]) * 60 + int(m[1])

min_required = correct_min - current_min
ans = 0
for i in [60, 15, 5, 1]:
    ans += min_required // i
    min_required %= i

return (ans)