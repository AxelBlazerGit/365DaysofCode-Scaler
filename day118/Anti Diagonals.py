class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers

    def diagonal(self, A):
        n = len(A)
        result = []

        for i in range(n):
            j = i
            l = 0
            row = []

            while j >= 0 and l < n:
                row.append(A[j][l])
                j -= 1
                l += 1

            result.append(row[::-1])

        for i in range(1, n):
            j = n - 1
            l = i
            col = []

            while l < n and j >= 0:
                col.append(A[j][l])
                j -= 1
                l += 1

            result.append(col[::-1])

        return result



