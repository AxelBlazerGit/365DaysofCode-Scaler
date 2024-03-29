int Solution::maxProfit(const vector<int> &A) {
    int ans=0;
    for(int i=1;i<A.size();i++)
        ans+=(A[i]-A[i-1]>0)?A[i]-A[i-1]:0;
    return ans;
}
