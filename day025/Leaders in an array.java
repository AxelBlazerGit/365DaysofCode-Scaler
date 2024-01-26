import java.util.*;

public class Solution {
    public int[] solve(int[] A) {
        int n = A.length;
        ArrayList<Integer> leaders = new ArrayList<>();
        int maxRight = A[n - 1];
        leaders.add(maxRight);

        for (int i = n - 2; i >= 0; i--) {
            if (A[i] > maxRight) {
                maxRight = A[i];
                leaders.add(maxRight);
            }
        }

        int[] result = new int[leaders.size()];
        for (int i = 0; i < leaders.size(); i++) {
            result[i] = leaders.get(i);
        }

        return result;
    }
}
