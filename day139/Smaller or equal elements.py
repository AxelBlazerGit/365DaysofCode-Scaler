class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        left = 0
        right = len(A) - 1
        count = 0

        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] <= B:
                count = mid + 1
                left = mid + 1
            else:
                right = mid - 1

        return count
