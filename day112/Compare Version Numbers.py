class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        max_dots = max(A.count("."), B.count("."))
        A, B = (A + ".0" * (max_dots - A.count("."))) if A.count(".") < max_dots else A, (B + ".0" * (max_dots - B.count("."))) if B.count(".") < max_dots else B
        a = [int(i) for i in A.split(".")]
        b = [int(j) for j in B.split(".")]
        # min_len = min(len(a), len(b))
        for i in range(len(a)):
            if a[i] > b[i]:
                return 1
            elif a[i] < b[i]:
                return -1
        if len(a) > len(b):
            return 1
        elif len(a) < len(b):
            return -1
        return 0
