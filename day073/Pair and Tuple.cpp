/*
#include <iostream>
#include <vector>
#include<tuple>
using namespace std;
*/

pair<int, int> findMaxMin(vector<int> &A){
    // First value of pair will be Maximum of array A and second will be Minimum of array A
    int maxVal = A[0];
    int minVal = A[0];
    
    for(int i = 1; i < A.size(); ++i){
        maxVal = max(maxVal, A[i]);
        minVal = min(minVal, A[i]);
    }
    
    return make_pair(maxVal, minVal);
}

tuple<int, int, int> compute(vector<int> &A){
    // First value of tuple will be sum of array A
    // Second value of tuple will be sum of even values in array A 
    // Third value of tuple will be sum of odd values in array A
    int sum = 0;
    int sumEven = 0;
    int sumOdd = 0;
    
    for(int i = 0; i < A.size(); ++i){
        sum += A[i];
        if(A[i] % 2 == 0)
            sumEven += A[i];
        else
            sumOdd += A[i];
    }
    
    return make_tuple(sum, sumEven, sumOdd);
}

/*
int main()  {
    int n;
    cin>>n;
    vector<int> A(n);
    for(int i = 0; i < n; i++){
        cin>>A[i];
    }
    
    pair<int, int> max_min = findMaxMin(A);
    cout<<max_min.first<<" "<<max_min.second<<endl;
    
    tuple<int, int, int> tuple_values = compute(A);
    cout<< get<0>(tuple_values) << " " << get<1>(tuple_values) << " " << get<2>(tuple_values) << endl;
    
    return 0;
}
*/
