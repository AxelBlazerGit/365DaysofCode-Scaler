class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def possible(self, mid, pages, count):
        curr = 0
        partition = 1
        for i in range(len(pages)):
            if curr + pages[i] <= mid:
                curr += pages[i]
            else:
                partition += 1
                curr = pages[i]
        return partition <= count
    
    def books(self, A, B):
        if len(A) < B:
            return -1
        s = max(A)
        e = sum(A)
        ans = -1
        while s <= e:
            mid = (s + e) // 2
            if self.possible(mid, A, B):
                ans = mid
                e = mid - 1
            else:
                s = mid + 1
        return ans

# if __name__ == "__main__":
#     A = [5, 17, 100, 11]
#     B = 4
#     solution = Solution()
#     result = solution.books(A, B)
#     print("Minimum number of pages a student can read:", result)
