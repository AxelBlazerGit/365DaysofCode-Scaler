class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)
        for i in range(n):
            for j in range(i, n):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        for i in range(n):
            l, r = 0, n - 1
            while l < r:
                A[i][l], A[i][r] = A[i][r], A[i][l]
                l += 1
                r -= 1
        
        return A
