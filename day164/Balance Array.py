class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        ans = 0
        evens = 0
        odds = 0
        leftEvens = [0] * n
        leftOdds = [0] * n

        for i in range(n):
            if i % 2 == 0:
                evens += A[i]
                leftEvens[i] = evens
                leftOdds[i] = leftOdds[i - 1] if i > 0 else 0
            else:
                odds += A[i]
                leftOdds[i] = odds
                leftEvens[i] = leftEvens[i - 1] if i > 0 else 0

        for i in range(n):
            currEven = (leftEvens[i - 1] if i > 0 else 0) + (odds - leftOdds[i])
            currOdd = (leftOdds[i - 1] if i > 0 else 0) + (evens - leftEvens[i])
            if currEven == currOdd:
                ans += 1

        return ans
