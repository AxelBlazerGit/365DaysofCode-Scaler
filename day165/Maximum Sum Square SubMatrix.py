class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        prefix_sum = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                prefix_sum[i][j] = A[i][j]
                if i > 0:
                    prefix_sum[i][j] += prefix_sum[i-1][j]
                if j > 0:
                    prefix_sum[i][j] += prefix_sum[i][j-1]
                if i > 0 and j > 0:
                    prefix_sum[i][j] -= prefix_sum[i-1][j-1]
        max_sum = float('-inf')
        for i in range(B - 1, N):
            for j in range(B - 1, N):
                total = prefix_sum[i][j]
                if i >= B:
                    total -= prefix_sum[i - B][j]
                if j >= B:
                    total -= prefix_sum[i][j - B]
                if i >= B and j >= B:
                    total += prefix_sum[i - B][j - B]
                
                max_sum = max(max_sum, total)
        return max_sum
