class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        hashA = {}
        hashB = {}
        hashC = {}
        for num in A:
            hashA[num] = 1
        for num in B:
            hashB[num] = 1
        for num in C:
            hashC[num] = 1
        ans = {}
        for num in hashA:
            if num in hashB or num in hashC:
                ans[num] = 1

        for num in hashB:
            if num in hashA or num in hashC:
                ans[num] = 1

        for num in hashC:
            if num in hashA or num in hashB:
                ans[num] = 1
        return sorted(ans.keys())
