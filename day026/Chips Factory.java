import java.util.ArrayList;

public class Solution {
    public ArrayList<Integer> solve(ArrayList<Integer> A) {
        int n = A.size();
        int nonEmptyIndex = 0;
        
        for (int i = 0; i < n; i++) {
            if (A.get(i) != 0) {
                A.set(nonEmptyIndex++, A.get(i));
            }
        }
        
        for (int i = nonEmptyIndex; i < n; i++) {
            A.set(i, 0);
        }
        return A;
    }
}
