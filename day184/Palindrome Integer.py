class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        if A<0:
            return 0
        A=str(A)
        return 1 if A==A[::-1] else 0
