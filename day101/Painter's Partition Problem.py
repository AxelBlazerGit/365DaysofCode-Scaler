class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def partition(self, arr, mid):
        allocated = 0
        partitions = 1
        for i in range(len(arr)):
            if allocated + arr[i] <= mid:
                allocated += arr[i]
            else:
                partitions += 1
                allocated = arr[i]
        return partitions
        
    def paint(self, painters, timeUnit, arr):
        low = max(arr)
        high = sum(arr)
        while low <= high:
            mid = (high + low) // 2
            if self.partition(arr, mid) > painters:
                low = mid + 1
            else:
                high = mid - 1
        return (low * timeUnit) % 10000003
