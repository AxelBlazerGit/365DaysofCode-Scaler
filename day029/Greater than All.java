public class Solution {
    public int solve(int[] A) {
        int count = 1, max = A[0];
        for (int i = 1; i < A.length; i++) {
            if (A[i] > max) {
                max = A[i];
                count++;
            }
        }
        return count;
    }
}
