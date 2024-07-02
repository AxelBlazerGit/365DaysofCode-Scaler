import heapq
class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        ans = []
        min_heap = []

        for row in A:
            for num in row:
                heapq.heappush(min_heap, num)

        while min_heap:
            ans.append(heapq.heappop(min_heap))

        return ans
