class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        count=0
        for i in range(len(A)):
            if(A[i]!=0):
                A[count]=A[i]
                count+=1
            
        while count<len(A):
            A[count]=0
            count+=1
        return A
