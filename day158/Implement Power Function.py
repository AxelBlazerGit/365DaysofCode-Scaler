class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        if x==0 and n==0 and d==1:
            return 0
        if n==1:
            return x%d
        if n==0:
            return 1
        temp=self.pow(x,n//2,d)%d
        if n%2:
            
            return (x*temp*temp)%d
        else:
            return (temp**2)%d
            
