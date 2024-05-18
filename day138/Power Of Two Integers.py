from math import sqrt

class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if A==1:
            return 1
        sqrtt = int(sqrt(A)) + 1
        for x in range(2, sqrtt):
            for p in range(2, 33):
                temp = x ** p
                if temp == A:
                    return 1
                if temp < A:
                    continue
                break
        return 0
