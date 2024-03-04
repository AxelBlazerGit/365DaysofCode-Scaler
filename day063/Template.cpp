/*
#include <iostream>
using namespace std;
*/

// Your code goes here
template <typename T>
int index_of_largest(const T arr[], int size) {
    if (size <= 0) {
        cerr << "Error: Array size must be greater than 0." << endl;
        return -1;  // Return an invalid index in case of an error
    }

    int maxIndex = 0;
    for (int i = 1; i < size; i++) {
        if (arr[i] > arr[maxIndex]) {
            maxIndex = i;
        }
    }

    return maxIndex;
}






/*
int main()  {
    int n;
    cin>>n;
    int arr_int[n];
    for(int i = 0; i < n; i++){
        cin>>arr_int[i];
    }
    int res = index_of_largest<int>(arr_int, n);
    cout<<res<<endl;
    
    cin>>n;
    double arr_double[n];
    for(int i = 0; i < n; i++){
        cin>>arr_double[i];
    }
    res = index_of_largest<double>(arr_double, n);
    cout<<res<<endl;
    return 0;
}
*/
