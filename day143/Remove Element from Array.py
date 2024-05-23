class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        n = len(A)
        i = 0
        j = 0
        ans = 0
        while j < n:
            if A[j] == B:
                j += 1
            else:
                A[i], A[j] = A[j], A[i]
                i += 1
                j += 1
                ans += 1
        return ans
            
