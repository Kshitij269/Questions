for i in range(int(input())):
    l=[]
    pw=1
    n=int(input())
    while(n):
        if n%10:
            s=int((n%10)*pw)
            l.append(s)
        n=int(n/10)
        pw=pw*10
    print(len(l))
    print()
    for i in l:
        print(i,end=" ")
    print()
    
