int Solution::removeDuplicates(vector<int> &A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    set<int> setF;
    for(int i=0;i<A.size();i++) setF.insert(A[i]);
    // return setF.size();
    A.clear();
    for(auto it:setF) A.push_back(it);
    return A.size();
}
