class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        i=1
        while i*(i+1)/2<=A:
            i+=1
        return i-1
