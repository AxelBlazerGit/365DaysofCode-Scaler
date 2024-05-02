class Solution:
	# @param A : list of integers
	# @param B : list of integers
	def merge(self, A, B):
        for i in B:
            A.append(i)
        A.sort()
