#include<iostream>

using namespace std;

int main()  {
    int x, y;
    cin>> x >> y;
    // YOUR CODE GOES HERE
    string g = (x <= y)? "Robin" : "Rahul";
    cout<< g;
    return 0;
}
