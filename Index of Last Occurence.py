def lastOccurence(arr,x):
    n= len(arr)
    low = 0
    high = n-1
    while (low<=high):
        mid = (low+high)//2
        if arr[mid]>x:
            high=mid-1
        elif arr[mid]<x:
            low = mid+1
        else :
            try:
                if (mid==0 or (arr[mid+1]!=arr[mid])):
                    return mid
                else:
                    low = mid+1
            except IndexError :
                return high
    return -1

arr=[2,3,4]
x=4
print(lastOccurence(arr,x))
