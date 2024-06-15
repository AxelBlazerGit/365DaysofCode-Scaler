class Solution:
    # @param A : list of integers
    # @return a float
    def solve(self, A):
        n = len(A)
        if n == 0:
            return 0.0
        average = sum(A) / n
        variance = 0.0
        for i in A:
            variance += (i - average) ** 2
        variance/=n
        return "{:.2f}".format(variance)
