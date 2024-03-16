bool comp(pair<int, int> a, pair<int, int> b) {
    return (a.first + a.second) < (b.first + b.second);
}
void sortArray(vector<pair<int, int>> &A){
    sort(A.begin(), A.end(), comp);
}
