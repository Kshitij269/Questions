class Solution:

    # Function to sort the binary array.
    def binSort(self, A, N):
        left = 0
        right = N - 1

        # Traverse the array
        while left < right:
            # Increment left index while we see 0 at left
            while left < right and A[left] == 0:
                left += 1

            # Decrement right index while we see 1 at right
            while left < right and A[right] == 1:
                right -= 1

            # If there is a 1 at left and a 0 at right, swap them
            if left < right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        return A
