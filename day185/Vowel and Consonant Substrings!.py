class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        ans=0
        mod=10**9+7
        vowels = set("aeiou")
        for i in A:
            if i in vowels:
                ans+=1
                ans%=mod
        return (ans*(len(A)-ans))%mod
