# import re
# class Solution:
#     # @param A : string
#     # @return a list of strings
#     def deserialize(self, A):
#         return re.findall(r'[a-zA-Z]+', A)
class Solution:
    # @param A : string
    # @return a list of strings
    def deserialize(self, A):
        ans=[]
        temp=""
        for i in A:
            if 'a'<=i<='z':
                temp+=i
            else:
                if temp!="":
                    ans.append(temp)
                temp=""
        # ans.append(temp)
        return ans
