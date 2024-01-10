import java.util.ArrayList;

public class Solution {
    public int solve(ArrayList<Integer> A) {
        if (A == null || A.isEmpty()) {
            return 0;
        }

        int n = A.size();
        int maxElement = Integer.MIN_VALUE;
        int minElement = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            int currentElement = A.get(i);
            if (currentElement > maxElement) {
                maxElement = currentElement;
            }
            if (currentElement < minElement) {
                minElement = currentElement;
            }
        }
        int result = maxElement + minElement;

        return result;
    }
}
