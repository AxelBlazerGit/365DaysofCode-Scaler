class Solution:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):
        n = len(A)
        left_max = [0] * n
        right_min = [0] * n

        left_max[0] = A[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], A[i])

        right_min[n - 1] = A[n - 1]
        for i in range(n - 2, -1, -1):
            right_min[i] = min(right_min[i + 1], A[i])

        for i in range(1, n - 1):
            if A[i] > left_max[i - 1] and A[i] < right_min[i + 1]:
                return 1

        return 0

