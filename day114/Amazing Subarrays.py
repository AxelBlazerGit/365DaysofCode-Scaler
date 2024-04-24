class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        ans=0
        for i in range(len(A)):
            if A[i] in "aeiouAEIOU":
                ans+=len(A)-i
        return ans%10003
