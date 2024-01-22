public class Solution {
    public String solve(String A) {
        StringBuilder result = new StringBuilder();
        int[] frequency = new int[26];

        for (char ch : A.toCharArray()) {
            frequency[ch - 'a']++;
        }

        for (char ch : A.toCharArray()) {
            int index = ch - 'a';
            if (frequency[index] > 0) {
                result.append(ch).append(frequency[index]);
                frequency[index] = 0; //character appended and removed from frequency data
            }
        }

        return result.toString();
    }
}
