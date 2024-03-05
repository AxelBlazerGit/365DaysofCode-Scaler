/*
#include<iostream>
#include<sstream>
using namespace std;
*/

int main()  {
    string A;
    cin>>A;
    // YOUR CODE GOES HERE
    int num;
    stringstream ss(A);
    while (getline(ss, A, ',')) {
        // Convert the extracted string to an integer
        stringstream convert(A);
        convert >> num;

        // Print the integer
        cout << num << endl;
    }
    
    return 0;
}
