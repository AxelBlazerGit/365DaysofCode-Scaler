class Solution:
    # @param A : integer
    # @param B : integer
     # @return an long
    def solve(self, A, B):
        num = A
        
        for _ in range(1, B):
            if num % 2 == 0:
                num //= 2
            else:
                num = 3 * num + 1
        
        return num
