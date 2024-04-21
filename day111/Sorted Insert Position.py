class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        s,e=0,len(A)-1
        while(s<=e):
            mid=(s+e)//2
            if A[mid]==B:
                return mid
            elif A[mid]>B:
                e=mid-1
            else:
                s=mid+1
        return s
