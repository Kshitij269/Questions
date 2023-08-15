class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = len(arr1)

        for i in arr1:
            low = 0
            high = len(arr2)-1
            while (high >= low):
                mid = (high + low) // 2
                if abs(i-arr2[mid]) <=d:
                    count-=1
                    break
                elif (i < arr2[mid]):
                    high = mid - 1
                elif i>arr2[mid]:
                    low = mid + 1

        return (count)
