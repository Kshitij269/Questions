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


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:

            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res
