class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        count_A = {}
        count_B = {}
        
        for i in A:
            count_A[i] = count_A.get(i, 0) + 1
        
        for i in B:
            count_B[i] = count_B.get(i, 0) + 1
        
        ans = []
        
        for i in set(A):
            if i in count_A and i in count_B:
                ans.extend([i] * min(count_A[i], count_B[i]))
        
        return ans
