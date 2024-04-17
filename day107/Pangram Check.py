#code
# print("GfG")
class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        check = [0]*26
        for word in A:
            for char in word:
                check[ord(char) - ord('a')] = 1
        return 1 if 0 not in check else 0
