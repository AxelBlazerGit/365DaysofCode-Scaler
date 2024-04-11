#code
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, a):
        s=0
        e=a
        ans=-1
        while(s<=e):
            mid=(s+e)//2
            if mid**2<=a:
                ans=mid
                s=mid+1
            else:
                e=mid-1
        return ans
    # print(sqrt(int(input())))
# solution = Solution()
# print(solution.sqrt(int(input())))
