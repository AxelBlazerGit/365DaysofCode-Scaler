class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        i=2
        if A==1:
            return 0
        while(i*i<=A):
            if A%i==0:
                return 0
            i+=1
        return 1
