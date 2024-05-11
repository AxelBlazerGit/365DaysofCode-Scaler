class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def addNumbers(self, A, B):
        while B:
            carry=A&B
            A^=B
            B=carry<<1
        return A
