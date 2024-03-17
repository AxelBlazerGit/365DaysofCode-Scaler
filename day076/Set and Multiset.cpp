#include<iostream>
#include<set>
#include<iterator>
using namespace std;

int main()  {
    // YOUR CODE GOES HERE
    // Please take input and print output to standard input/output (stdin/stdout)
    // E.g. 'cin' for input & 'cout' for output
    int Q;
    cin >> Q;

    set<int> s;
    
    for (int i = 0; i < Q; i++) {
        int y, x;
        cin >> y >> x;

        if (y == 1) {
            s.insert(x);
        } else if (y == 2) {
            s.erase(x);
        } else if (y == 3) {
            if (s.find(x) != s.end()) {
                cout << "Yes" << endl;
            } else {
                cout << "No" << endl;
            }
        }
    }

    if (!s.empty()) {
        for (auto it = s.begin(); it != s.end(); it++) {
            cout << *it << endl;
        }
    }

    return 0;
}
