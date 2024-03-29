vector<int> Solution::solve(vector<int> &A, vector<int> &B) {
    vector<int > ans;
    for(int i=0;i<B.size();i++){
        int idx=-1;
        for(int iter=0;iter<A.size();iter++){
            if(A[iter]>=B[i]){
                idx=iter;
                break;
            }
        }
        ans.push_back(idx);
    }
    return ans;
}
