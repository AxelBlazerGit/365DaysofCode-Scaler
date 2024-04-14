class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        low = 0
        mid = 0
        high = len(A) - 1
        
        while mid <= high:
            if A[mid] == 0:
                # Swap A[mid] and A[low]
                A[mid], A[low] = A[low], A[mid]
                mid += 1
                low += 1
            elif A[mid] == 1:
                mid += 1
            else:
                # Swap A[mid] and A[high]
                A[mid], A[high] = A[high], A[mid]
                high -= 1
