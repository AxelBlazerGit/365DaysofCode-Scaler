class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, year):
        if year % 4 == 0:  
            if year % 100 == 0:  
                if year % 400 == 0:  
                    return 1
                else:
                    return 0
            else:
                return 1
        else:
            return 0
