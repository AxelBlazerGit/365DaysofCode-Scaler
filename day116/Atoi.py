class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        ans = 0
        neg = False
        dig = False
        for i in A:
            if i == '+':
                continue
            if ans == 0 and i == '-' and dig == False:
                neg = True
                continue
            if ans == 0 and i != ' ' and i not in "0123456789" and i != '+':
                return 0
            if i in "0123456789":
                dig = True
                ans *= 10
                ans += int(i)
                # Check for overflow
                if not neg and ans > 2147483647:
                    return 2147483647
                elif neg and ans > 2147483648:
                    return -2147483648
            else:
                break
        return ans if neg == False else -ans
