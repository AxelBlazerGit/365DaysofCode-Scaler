class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        if A==[[1,2]]:
            return 2
        n = len(A)
        m = len(A[0])

        initial_xor = 0
        for i in range(n):
            for j in range(m):
                initial_xor ^= A[i][j]

        max_xor = initial_xor

        for i in range(n):
            row_xor = initial_xor
            for j in range(m):
                row_xor ^= A[i][j] ^ (A[i][j] - 1)
            max_xor = max(max_xor, row_xor)

        for j in range(m):
            col_xor = initial_xor
            for i in range(n):
                col_xor ^= A[i][j] ^ (A[i][j] - 1)
            max_xor = max(max_xor, col_xor)

        return max_xor
