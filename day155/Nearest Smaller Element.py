class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        ans = [-1] * len(A)
        stk = []
        for i in range(len(A)):
            while stk and stk[-1] >= A[i]:
                stk.pop()
            ans[i] = -1 if not stk else stk[-1]
            stk.append(A[i])
        return ans
