class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        p=1
        for i in str(A):
            p*=int(i)
        return p
