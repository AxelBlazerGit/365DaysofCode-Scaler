from collections import Counter
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        freq=Counter(A)
        for key,val in freq.items():
            if val>len(A)//2:
                return key
        return 0
