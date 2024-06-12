class Solution:
	# @param A : integer
	# @return a list of strings
	def fizzBuzz(self, A):
        ans=[]
        for i in range(1,A+1):
            if i%15==0:
                ans.append("FizzBuzz")
                # continue
            elif i%5==0:
                ans.append("Buzz")
            elif i%3==0:
                ans.append("Fizz")
            else:
                ans.append(i)
        return ans
