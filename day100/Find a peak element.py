class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if sorted(A) == A:
            return A[-1]
        if sorted(A) == A[::-1]:
            return A[0]
        s = 0
        e = len(A) - 1
        if e == 2:
            return e - 1
        while s < e:
            mid = int(s + (e - s) / 2)
            if A[mid] > A[mid - 1] and A[mid + 1] < A[mid]:
                return A[mid]
            if A[mid] > A[mid - 1]:
                s = mid
            else:
                e = mid
        return A[s]  # just to adjust syntax
