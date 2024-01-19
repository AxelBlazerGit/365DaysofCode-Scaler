class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        lst=[0,0]
        for i in A:
            if i>0:
                lst[0]+=1
            if i<0:
                lst[1]+=1
                
        return lst
