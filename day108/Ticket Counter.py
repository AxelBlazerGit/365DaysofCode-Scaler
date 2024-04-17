class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        time = 0  
        ans = 0
        for i in range(len(A)):
            if A[i] < time:
                ans += 1
            else:
                time += B[i]
        return ans
