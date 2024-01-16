import java.util.ArrayList;

public class Solution {
    public ArrayList<Integer> solve(String A) {
        int[] frequency = new int[26];
        
        for (int i = 0; i < A.length(); i++) {
            char currentChar = A.charAt(i);
            
            if (currentChar >= 'a' && currentChar <= 'z') {
                frequency[currentChar - 'a']++;
            }
        }
        
        ArrayList<Integer> result = new ArrayList<>();
        for (int count : frequency) {
            result.add(count);
        }
        
        return result;
    }
}
