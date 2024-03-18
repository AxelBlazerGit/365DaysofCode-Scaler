#include<iostream>
#include<map>
using namespace std;

int main()  {
    // YOUR CODE GOES HERE
    // Please take input and print output to standard input/output (stdin/stdout)
    // E.g. 'cin' for input & 'cout' for output
    int Q;
    cin >> Q;
    
    map<int, int> boxes; 
    for(int i = 0; i < Q; ++i) {
        int type;
        cin >> type;
        
        if(type == 1) {
            int X, Y;
            cin >> X >> Y;
            boxes[X] += Y; } else if(type == 2) {
            int X;
            cin >> X;
            boxes[X] = 0; // Remove all balls from box X
        } else if(type == 3) {
            int X;
            cin >> X;
            cout << boxes[X] << endl; // Print the number of balls in box X
        }
    }
    
    return 0;
}
