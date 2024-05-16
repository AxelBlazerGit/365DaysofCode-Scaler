class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        first = firstOcc(A, B)
        last = lastOcc(A, B)
        if first == -1 or last == -1:
            return 0
        return last - first + 1

def firstOcc(A, B):
    s = 0
    e = len(A) - 1
    ans = -1
    while s <= e:
        mid = (s + e) // 2
        if A[mid] == B:
            ans = mid
            e = mid - 1
        elif A[mid] < B:
            s = mid + 1
        else:
            e = mid - 1
    return ans

def lastOcc(A, B):
    s = 0
    e = len(A) - 1
    ans = -1
    while s <= e:
        mid = (s + e) // 2
        if A[mid] == B:
            ans = mid
            s = mid + 1
        elif A[mid] < B:
            s = mid + 1
        else:
            e = mid - 1
    return ans

# class Solution:
#     # @param A : tuple of integers
#     # @param B : integer
#     # @return an integer
#     def findCount(self, A, B):
#         return lastOcc(A, B) - firstOcc(A, B) + 1 if (lastOcc(A, B) - firstOcc(A, B))!=0 else 0
