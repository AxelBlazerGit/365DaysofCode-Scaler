#include<iostream>
#include<iomanip> 

using namespace std;

int main() {
    // Declare variables to store input values
    int integerVal;
    long longVal;
    char charVal;
    float floatVal;
    double doubleVal;

    // Input values
    cin >> integerVal >> longVal >> charVal >> floatVal >> doubleVal;

    // Output values with specific formatting
    cout << integerVal << endl;
    cout << longVal << endl;
    cout << charVal << endl;
    cout << fixed << setprecision(3) << floatVal << endl;  // Print float up to 3 decimal places
    cout << fixed << setprecision(9) << doubleVal << endl; // Print double up to 9 decimal places

    return 0;
}
