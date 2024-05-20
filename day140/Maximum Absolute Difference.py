class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        sumMax=-float('inf')
        sumMin=float('inf')
        negateMax=-float('inf')
        negateMin=float('inf')
        for idx,ele in enumerate(A):
            sumMax=max(sumMax,(ele+idx))
            sumMin=min(sumMin,(ele+idx))
            negateMax=max(negateMax,(ele-idx))
            negateMin=min(negateMin,(ele-idx))
        return max(sumMax-sumMin,negateMax-negateMin)
