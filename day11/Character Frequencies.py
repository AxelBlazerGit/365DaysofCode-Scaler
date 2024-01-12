class Solution:
    def solve(self, A):
        result = {}
        for i in A:
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
        return list(result.values())
