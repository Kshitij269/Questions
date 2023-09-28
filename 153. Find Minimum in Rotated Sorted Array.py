nums = [3,4,5,1,2]
def search(nums):
    low= 0
    high = len(nums)-1
    ans = 10000000000000000
    while (high>=low):
        mid = (high+low)//2
        if (nums[low] <= nums[mid]):
            ans = min(ans ,nums[low])
            low = mid+1
        else :
            high = mid-1
            ans = min(ans,nums[mid])
    return ans
print(search(nums))