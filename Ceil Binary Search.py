arr=[-2,-1,-1,1,2,3]
target=int(input())
def ceil(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid = low + (high-low)//2
        if arr[mid]<target:
            low=mid+1
        elif arr[mid]>target:
            high=mid-1
        else:
            return mid
    return low

print(ceil(arr,target))
