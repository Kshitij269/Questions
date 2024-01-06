class Solution:
    def kthElement(self, arr1, arr2, n, m, k):
        i = 0
        j = 0
        cnt = 1
        arr3 = []

        while i < n and j < m:
            if arr1[i] < arr2[j]:
                cnt += 1
                arr3.append(arr1[i])
                i += 1
            else:
                cnt += 1
                arr3.append(arr2[j])
                j += 1

        while i < n:
            cnt += 1
            arr3.append(arr1[i])
            i += 1

        while j < m:
            cnt += 1
            arr3.append(arr2[j])
            j += 1

        return arr3[k]

# Example usage:
solution = Solution()
arr1 = [2, 3, 4, 7]
arr2 = [1, 5, 6]
n = len(arr1)
m = len(arr2)
k = 4
result = solution.kthElement(arr1, arr2, n, m, k)
print(result)
