class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        return (int(A[-1])**(int(B)%4))%10 if int(B)%4!=0 else (int(A[-1])**4)%10
