import re
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        words = re.findall(r'\S+', A)
        words.reverse()
        A= ' '.join(words)
        
        return A
