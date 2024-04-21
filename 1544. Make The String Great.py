class Solution:
    def makeGood(self, s: str) -> str:
        l=[]
        l.append(s[0])
        for i in s[1:len(s)]:
            try:
                if l[-1].islower() and i==l[-1].upper():
                    l.pop()
                elif l[-1].isupper() and i==l[-1].lower():
                    l.pop()
                else:
                    l.append(i)
            except IndexError:
                l.append(i)

        return(''.join(l))
