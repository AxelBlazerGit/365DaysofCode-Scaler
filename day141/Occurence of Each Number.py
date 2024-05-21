class Solution:
    # @param A : list of integers
    # @return a list of integers
    def findOccurences(self, A):
        freq = {}
        for idx, ele in enumerate(A):
            if ele not in freq:
                freq[ele] = [idx, 1]
            else:
                freq[ele][1] += 1
        elements_and_freq = []
        for key in freq:
            elements_and_freq.append((key, freq[key][1]))
        elements_and_freq.sort()
        result = [freq for ele, freq in elements_and_freq]
        
        return result
