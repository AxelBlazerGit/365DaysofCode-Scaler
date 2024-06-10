class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        return (2**(len(A))-1)%(10**9+7)
        # return x - 1
