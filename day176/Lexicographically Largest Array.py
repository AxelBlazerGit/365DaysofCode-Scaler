class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        prefix_array = []
        suffix_array = []
        for i in range(0,n):
            if A[i]<A[n-1]:
                suffix_array = A[i:]
                break
            else:
                prefix_array.append(A[i])
        suffix_array.reverse()
        prefix_array.extend(suffix_array)
       
        return prefix_array
