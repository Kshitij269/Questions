def rec(ind,ds,s,sum,arr,n):
    if (ind==n):
        if s==sum:
            for i in arr:
                print(i,end=" ")
            print()
        return

    ds.append(arr[ind])
    s+=arr[ind]

    rec(ind+1,ds,s,sum,arr,n)

    s-=arr[ind]
    g=ds.pop()

    rec(ind+1,ds,s,sum,arr,n)

arr=[1,2,1]
sum = 2
n=3
ds=[]
rec(0,ds,0,sum,arr,n)

