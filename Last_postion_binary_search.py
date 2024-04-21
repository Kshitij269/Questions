def last_position(nums, target):
    lo, hi = 0, len(nums)
    while lo<=hi:
        mid = (lo+hi)//2
        if nums[mid] == target:
            if mid+1<len(nums) and nums[mid+1] == target:
                lo = mid+1
            else:
                return mid
        elif nums[mid]>target:
            hi = mid-1
        elif nums[mid]<target:
            lo = mid+1
    return -1