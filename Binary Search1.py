arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
ctr=0
arr2.sort()
for i in arr1:
    n=i
    start=0
    end=len(l)-1

    while start<=end:
        mid=start+(end-start)//2
        if l[mid]==n:
            print("Element Found At Index",mid)
            break
        elif l[mid]>n:
            end=mid-1
        else:
            start=mid+1
    else:
        print(-1)
