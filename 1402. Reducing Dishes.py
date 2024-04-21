def maxSatisfaction(satisfaction):
    satisfaction.sort()
    print(satisfaction)

    ans = res = 0

    while satisfaction:
        element = satisfaction.pop()
        if res + element < 0:  return ans

        print(res)
        res += element
        ans += res

    return ans


satisfaction = [-1, -8, 0, 5, -9]
l = maxSatisfaction(satisfaction)
print(l)
