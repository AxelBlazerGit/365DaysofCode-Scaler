class Solution:
	# @param A : string
	# @return an integer
    def fact(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.fact(n - 1)
	def findRank(self, A):
        n = len(A)
        rank = 1
        for i in range(n):
            smaller_in_right = 0
            for j in range(i + 1, n):
                if A[j] < A[i]:
                    smaller_in_right += 1
            rank += smaller_in_right * self.fact(n - i - 1)
        return rank%1000003
