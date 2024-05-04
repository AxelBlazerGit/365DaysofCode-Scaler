class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        def binSearchL(A, B):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if A[mid] == B:
                    if mid == 0 or A[mid - 1] < B:
                        return mid
                    right = mid - 1
                elif A[mid] < B:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        def binSearchR(A, B):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if A[mid] == B:
                    if mid == len(A) - 1 or A[mid + 1] > B:
                        return mid
                    left = mid + 1
                elif A[mid] < B:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        left_index = binSearchL(A, B)
        if left_index == -1:
            return [-1, -1]

        right_index = binSearchR(A, B)
        return [left_index, right_index]
