class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        if len(A) == 1:
            return A[0]
        if A == sorted(A):
            return A[0]
        return A[self.pivot(A) + 1]

    def pivot(self, A):
        s = 0
        e = len(A) - 1
        while s < e:
            mid = s + (e - s) // 2
            if A[mid] > A[e]:
                s = mid + 1
            else:
                e = mid
        return s - 1
