arr1=[4,5,8]
arr2=[10,9,1,8]

def binary(arr,target):
    low=0
    high=len(arr)-1
    arr.sort()
    print(arr)
    while low<=high:
        mid = low+(high-low)//2
        if arr[mid]<target:
            low=mid+1
        elif arr[mid]>target:
            high=mid-1
        else:
            return len(arr[0:mid])
    return low

for i in arr1:
    print(binary(arr2,i))
        
