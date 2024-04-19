class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        ans = ""

        while A:
            mod = A % 26
            if mod == 0:
                ans += 'Z'
                A = A // 26 - 1
            else:
                ans += chr(ord('A') + mod - 1)
                A = A // 26

        return ans[::-1]
