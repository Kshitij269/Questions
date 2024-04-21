class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        nums.sort()
        low = 0
        high = len(nums)-1
        while high >= low :
            mid = low + (high-low)//2
            if nums[mid] == target :
                ans.append(mid)
                i = mid-1
                while i>= low and nums[i] == target:
                    ans.append(i)
                    i-=1
                i = mid+1
                while i<=high and nums[i] == target :
                    ans.append(i)
                    i+=1
                break
            elif nums[mid] < target :
                low = mid+1
            else :
                high = mid -1
        ans.sort()
        return ans 