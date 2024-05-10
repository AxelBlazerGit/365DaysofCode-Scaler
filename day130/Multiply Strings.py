class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def multiply(self, A, B):
        a,b=0,0
        for i in A:
            a=a*10+int(i)
        for i in B:
            # if b>0 and int(i)>-1:
            b=b*10+int(i)
        return str(a*b)
