class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        temp = {}
        repeats = {}
        for idx, val in enumerate(A):
            if val in temp:
                if val not in repeats:
                    repeats[val] = temp[val]
                elif idx < repeats[val]:
                    repeats[val] = idx
            else:
                temp[val] = idx
        if repeats:
            min_key = min(repeats, key=lambda k: repeats[k])
            return min_key
        else:
            return -1
