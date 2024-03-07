/*
#include<iostream>
using namespace std;
*/

void solve(int *A, int *B){
int originalA = *A;
    int originalB = *B;

    // Modify values in memory
    *A = originalA + originalB;
    *B = abs(originalA - originalB);
}



/*
int main()  {
    int A, B;
    int *pA = &A, *pB = &B;
    cin>>A>>B;
    solve(pA, pB);
    cout<<A<<endl;
    cout<<B<<endl;
    return 0;
}
*/
