arr=[2,3,5,9,14,16,18]
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
    return low,high

print(ceil(arr,target))
