class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLongestSubstring(self, A):
        temp={}
        ans,s=0,0
        for i in range(len(A)):
            ch=A[i]
            if ch in temp and temp[ch]>=s:
                s=temp[ch]+1
            temp[ch]=i
            ans=max(ans,i-s+1)
        return ans
