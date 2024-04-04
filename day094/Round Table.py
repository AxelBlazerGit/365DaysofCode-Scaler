class Solution:
    # @param A : integer
    # @return an integer
    def f(self, n):
        result = 1
        for i in range(2, n + 1):
            result = (result * i) % (10**9 + 7)
        return result
    def solve(self, A):
        return int(2 * self.f(A) % (10**9 + 7))
