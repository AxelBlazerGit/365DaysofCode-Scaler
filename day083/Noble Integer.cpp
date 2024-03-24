int Solution::solve(vector<int> &A) {
    sort(A.begin(), A.end());
    int n = A.size();
    for (int i = 0; i < n; ++i) {
        while(i+1<n and A[i]==A[i+1]) i++;
        long long count_greater = n - i - 1;
        if (A[i] == count_greater) {
            return 1;
        }
    }
    return -1;
}
