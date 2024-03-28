int Solution::solve(int A) {
    int c=0;
    while(A!=0){
        if(A&1) break;
        c++;
        A=A>>1;
    }
    return c;
}
