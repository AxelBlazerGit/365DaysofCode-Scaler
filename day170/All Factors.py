class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        ans = set()
        for i in range(1, int(A**0.5) + 1):
            if A % i == 0:
                ans.add(i)
                ans.add(A // i)
        return sorted(ans)
