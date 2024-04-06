#https://twitter.com/_AxelBlazer_/status/1776688303401537862
class Solution:
	# @param A : integer
	# @return an integer
	def trailingZeroes(self, A):
        # count+=A//
        count=0
        while(A>=5):
            A//=5
            count+=A
        return count
