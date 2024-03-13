#include<iostream>
#include<vector>
#include<algorithm>
#include<iterator>
using namespace std;

int main()  {
    // YOUR CODE GOES HERE
    // Please take input and print output to standard input/output (stdin/stdout)
    // E.g. 'cin' for input & 'cout' for output
    int N, Q;
    cin >> N;
    
    vector<int> arr(N);
    
    for (int i = 0; i < N; ++i) {
        cin >> arr[i];
    }
    
    cin >> Q;
    
    for (int i = 0; i < Q; ++i) {
        int X;
        cin >> X;
        
        auto leftmost = lower_bound(arr.begin(), arr.end(), X);
        int leftIndex = distance(arr.begin(), leftmost);

        auto rightmost = upper_bound(arr.begin(), arr.end(), X);
        int rightIndex = distance(arr.begin(), rightmost);

        if (leftIndex < N && arr[leftIndex] == X) {
            cout << leftIndex << endl;
        } else {
            cout << rightIndex << endl;
        }
    }
    return 0;
}
