nums = [-1, 1, 1, 2, 3]
target = 1
k = 0


def binarySearch(arr, target,i):
    low = 0
    high = len(arr)-1
    ans = -1
    while high >= low:
        mid = (high + low) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            ans = mid
            high = mid - 1
    print(arr,target)
    return ans-i


for i in range(len(nums)):
    print(k)
    k += binarySearch(nums[i:len(nums)], nums[i] + target,i)

print(k)


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        low = 0
        high = len(nums) - 1

        while low < high:
            if nums[low] + nums[high] < target:
                ans += high - low
                low += 1
            else:
                high -= 1

        return ans  