class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def addArrays(self, A, B):
        A=int(''.join(map(str, A)))
        B=int(''.join(map(str, B)))
        # A=int(A)
        # B=int(B)
        return list(map(int, str(A+B)))
        
