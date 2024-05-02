class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        c=0
        temp=[]
        for i in A:
            if i=='(':
                temp.append(i)
            elif len(temp)>0:
                temp.pop()
            else:
                c+=1
        return c+len(temp)
