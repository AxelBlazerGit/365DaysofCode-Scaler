class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        hash_table = {}
        ans = 0
        for num in A:
            hash_table[num] = True
        for num in hash_table:
            if B ^ num in hash_table:
                ans += 1
        return ans // 2

