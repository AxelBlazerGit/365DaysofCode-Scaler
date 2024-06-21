class Solution:
    # @param A : list of integers
    # @return an integer
    def divisibleBy60(self, A):
        if A==[0]:
            return 1
        if 0 not in A:
            return 0
        if sum(A) % 3 != 0 and sum(A)!=0:
            return 0
        return 1 if any(x != 0 and x % 2 == 0 for x in A) else 0
