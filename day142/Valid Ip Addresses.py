class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        n = len(A)  # Get the length of the input string
        ans = []  # Initialize the list to store valid IP addresses

        # Generate all possible splits for the IP address
        # The outer loop represents the position of the first dot
        for i in range(1, min(4, n)):
            # The middle loop represents the position of the second dot
            for j in range(i + 1, min(i + 4, n)):
                # The inner loop represents the position of the third dot
                for k in range(j + 1, min(j + 4, n)):
                    # Divide the string into 4 segments
                    s1 = A[:i]   # First segment
                    s2 = A[i:j]  # Second segment
                    s3 = A[j:k]  # Third segment
                    s4 = A[k:]   # Fourth segment

                    # Check if all segments are valid
                    if self.isOK(s1) and self.isOK(s2) and self.isOK(s3) and self.isOK(s4):
                        # If valid, join the segments with dots and add to the list
                        ans.append(".".join([s1, s2, s3, s4]))

        # Return the sorted list of valid IP addresses
        return sorted(ans)

    def isOK(self, segment):
        # Check if the segment is a valid IP segment
        if len(segment) > 1 and segment[0] == '0':
            return False  # Leading zero is not allowed
        return 0 <= int(segment) <= 255  # Check if the integer value is in the range [0, 255]
