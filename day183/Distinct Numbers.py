from collections import Counter
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        frequency = Counter(A)
        distinct_count = len(frequency)
        if distinct_count <= B:
            return 0
        frequencies = sorted(frequency.values())
        operations = 0
        for i in range(distinct_count - B):
            operations += frequencies[i]
        
        return operations
