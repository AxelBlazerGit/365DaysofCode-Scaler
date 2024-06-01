class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        temp = set()
        dupe = None
        for num in A:
            if num in temp:
                dupe = num
                break
            temp.add(num)
        
        n = len(A)
        actual_sum = sum(A)
        expected_sum = n * (n + 1) // 2
        
        missing = expected_sum - actual_sum + dupe
        
        return [dupe, missing]
