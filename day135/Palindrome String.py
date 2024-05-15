class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        new=""
        for i in A:
            if i.isalnum():
                new+=i if i.isnumeric() else i.lower()
        return 1 if new==new[::-1] else 0
