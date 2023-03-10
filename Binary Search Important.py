def bsearchstart(n,ele):
    start=0
    end = len(n)-1
    ans=-1
    
    while (start<=end):
        mid = start+(end-start)//2
        if n[mid]>ele:
            end=mid-1    
        elif n[mid]<ele:
            start=mid+1
        else:
            ans=mid
            end=mid-1

    return ans

def bsearchend(n,ele):
    start=0
    end = len(n)-1
    ans=-1
    
    while (start<=end):
        mid = start+(end-start)//2
        if n[mid]>ele:
            end=mid-1    
        elif n[mid]<ele:
            start=mid+1
        else:
            ans=mid
            start=mid+1

    return ans


nums = [5,6,7,8,8,8,8,8,8,8,8,9,10]
index1 = bsearchstart(nums,8)
index2 = bsearchend(nums,8)
l=[index1,index2]
print(l)
