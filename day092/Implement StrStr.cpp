int Solution::strStr(const string A, const string B) {
    int n = A.length();
    int m = B.length();

    if (m == 0) 
        return n == 0 ? 0 : -1;

    for (int i = 0; i <= n - m; ++i) {
        int j;
        for (j = 0; j < m; ++j) {
            if (A[i + j] != B[j])
                break;
        }
        if (j == m) 
            return i;
    }

    return -1; 
}
