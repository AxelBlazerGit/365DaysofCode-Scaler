def pivIdx(arr):
    s = 0
    e = len(arr) - 1
    while s < e:
        mid = (s + e) // 2
        if arr[mid] > arr[mid + 1]:
            return mid + 1
        elif arr[mid] >= arr[s]:
            s = mid + 1
        else:
            e = mid
    return s

def binSearch(arr, st, end, target):
    while st <= end:
        mid = st + (end - st) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            st = mid + 1
        else:
            end = mid - 1
    return -1

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        pv = pivIdx(A)
        left = binSearch(A, 0, pv-1, B)
        right = binSearch(A, pv, len(A) - 1, B)
        if left != -1:
            return left
        right_segment = A[pv:][::-1]
        right = binSearch(right_segment, 0, len(right_segment) - 1, B)
        if right != -1:
            return pv + len(right_segment) - 1 - right
        else:
            return -1
