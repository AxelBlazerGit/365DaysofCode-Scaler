from collections import Counter
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        frequency=Counter(A)
        ans=0
        for i in frequency:
            ans+=frequency[i]//2
        return ans
