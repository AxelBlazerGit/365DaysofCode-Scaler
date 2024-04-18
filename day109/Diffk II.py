class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        n = len(A)
        if n < 2:
            return 0
        
        processed = set()
        for num in A:
            if num - B in processed or num + B in processed:
                return 1
            processed.add(num)
        return 0
