
    def search(nums, target) :
        low = 0
        high = len(nums) - 1
        while high >= low:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid

            if (nums[low] <= nums[mid]):
                if (nums[low] <= target and nums[mid] > target):
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if (nums[high] >= target and nums[mid] < target):
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

print(search())