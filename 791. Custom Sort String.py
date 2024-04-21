class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d={}
        count =dict(Counter(s))
        for index,val in enumerate(order):
            d[val] = index

        ans = ["" for i in range(len(s))]
        np = -1
        for i in s:
            if i in d:
                ans[d[i]] = i*count[i]
            else:
                ans[np]=i
                np-=1
        return("".join(ans))

