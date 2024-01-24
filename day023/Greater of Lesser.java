public class Solution {
    public int solve() {
        return 0;  // no arguments are given
    }

    public int solve(int[] A) {
        return solve(A, new int[]{}, 0);
    }

    public int solve(int[] A, int[] B) {
        return solve(A, B, 0);
    }

    public int solve(int[] A, int[] B, int C) {
        int less = 0, more = 0;
        for (int i = 0; i < A.length; i++) {
            less += (A[i] > C) ? 1 : 0;
            more += (B[i] < C) ? 1 : 0;
        }
        return Math.max(less, more);
    }
}
