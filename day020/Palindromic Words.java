public class Solution {
    public int solve(String A) {
        String[] words = A.split("\\s+"); //split string for word array
        int palindromicCount = 0;
        for (String word : words) {
            if (isPalindrome(word)) {
                palindromicCount++;
            }
        }

        return palindromicCount;
    }

    private static boolean isPalindrome(String word) {
        int start = 0, end = word.length() - 1;
        while (start < end) {
            if (word.charAt(start) != word.charAt(end)) {
                return false;
            }
            start++;
            end--;
        }

        return true;
    }
}
