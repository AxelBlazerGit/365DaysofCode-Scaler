#include<iostream>
#include <vector>
#include<algorithm>
using namespace std;

int main()  {
    // YOUR CODE GOES HERE
    // Please take input and print output to standard input/output (stdin/stdout)
    // E.g. 'cin' for input & 'cout' for output
    int N;
    cin >> N;

    vector<int> v(N);

    for (int i = 0; i < N; ++i) {
        cin >> v[i];
    }

    int X;
    cin >> X;
    v.erase(v.begin() + X);
sort(v.begin(), v.end());
// Print the sorted vector
for (int i = 0; i < N - 1; ++i) {
    cout << v[i] << endl;
}

return 0;

    return 0;
}
