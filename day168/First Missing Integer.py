class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        hash = [0] * (n + 1)
        for i in A:
            if 1 <= i <= n:
                hash[i] = 1
        for idx in range(1, n + 1):
            if hash[idx] == 0:
                return idx
        return n + 1

