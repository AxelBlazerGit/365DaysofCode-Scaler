class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
        while self.gcd(A, B) != 1:
            A //= self.gcd(A, B)
        return A

    def gcd(self, B, X):
        while X != 0:
            B, X = X, B % X
        return B

# solution = Solution()
# print(solution.cpFact(int(input("Enter A: ")), int(input("Enter B: "))))
