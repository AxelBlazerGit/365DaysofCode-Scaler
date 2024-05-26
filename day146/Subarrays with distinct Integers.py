class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return self.countGood(A, B) - self.countGood(A, B - 1)
    
    def countGood(self, A, B):
        count = 0
        left = 0
        right = 0
        unique_count = 0
        freq = {}
        
        while right < len(A):
            if A[right] not in freq or freq[A[right]] == 0:
                unique_count += 1
            freq[A[right]] = freq.get(A[right], 0) + 1
            
            while unique_count > B:
                freq[A[left]] -= 1
                if freq[A[left]] == 0:
                    unique_count -= 1
                left += 1
            
            count += right - left + 1
            right += 1
        
        return count
'''
1. Define a class Solution:
    a. Define a method solve that takes input A (list of integers) and B (integer):
        i. Return the difference between the count of good subarrays with at most B different integers 
           and the count of good subarrays with at most B-1 different integers.

    b. Define a helper method countGood that takes input A (list of integers) and B (integer):
        i. Initialize variables:
            - count to store the count of good subarrays.
            - left and right pointers to define the current window.
            - unique_count to keep track of the number of unique elements in the window.
            - freq to maintain the frequency of elements in the window (initialized as an empty dictionary).

        ii. While the right pointer is less than the length of A:
            - If A[right] is not in freq or its frequency is 0, increment unique_count.
            - Update the frequency of A[right] in freq.
            
            - While unique_count is greater than B:
                - Decrement the frequency of A[left] in freq.
                - If the frequency becomes 0, decrement unique_count.
                - Move the left pointer to the right.

            - Update count by adding the length of the current window (right - left + 1).
            - Move the right pointer to the right.

        iii. Return the count.

2. Create an instance of the Solution class.
3. Test the solution with sample inputs.
'''
