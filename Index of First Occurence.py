def firstOccurence(arr,x):
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
            if (mid==0 or (arr[mid-1]!=arr[mid])):
                return mid
            else:
                high = mid-1
    return -1

arr=[1,2,3,4,5,5,5,5,5]
x=6
print(firstOccurence(arr,x))
