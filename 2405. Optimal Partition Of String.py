s = "abacaba"
di = {}
ans = 0
for i in range(len(s)):
    if s[i] in di:
        ans += 1
        di={}
    di[s[i]]=0

print(ans+1)
