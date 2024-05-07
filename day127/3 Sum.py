class Solution:
    def threeSumClosest(self, A, B):
        closest_sum = float('inf')
        min_diff = float('inf')
        N = len(A)
        A.sort()

        for i in range(N):
            left = i + 1
            right = N - 1
            
            while left < right:
                curr_sum = A[i] + A[left] + A[right]
                diff = abs(curr_sum - B)
                
                if diff < min_diff:
                    min_diff = diff
                    closest_sum = curr_sum
                
                if curr_sum < B:
                    left += 1
                elif curr_sum > B:
                    right -= 1
                else:
                    return B
                    
        return closest_sum
