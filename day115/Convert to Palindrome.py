class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        left, right = 0, n - 1
        
        def is_palindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        while left < right:
            if A[left] != A[right]:
                if is_palindrome(A, left + 1, right):
                    return 1
                if is_palindrome(A, left, right - 1):
                    return 1
                return 0
            left += 1
            right -= 1
            
        return 1
