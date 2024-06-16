import heapq
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        seats = [-x for x in A]
        heapq.heapify(seats)
        ans = 0
        for _ in range(B):
            top = -heapq.heappop(seats)
            ans += top
            heapq.heappush(seats, -(top - 1))
    
        return ans

