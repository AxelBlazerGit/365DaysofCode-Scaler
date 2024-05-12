class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        n = len(A)
        answer = []
        for rotate_by in B: 
            rotate_by %= n
            rotated_array = A[rotate_by:] + A[:rotate_by]
            answer.append(rotated_array)
        return answer


