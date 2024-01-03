public class Solution {
    public String longestCommonPrefix(ArrayList<String> a) {
        if (a == null || a.isEmpty()) {
            return "";
        }
        String prefix = a.get(0);

        for (int i = 1; i < a.size(); i++) {
            while (a.get(i).indexOf(prefix) != 0) {
                prefix = prefix.substring(0, prefix.length() - 1);

                if (prefix.isEmpty()) {
                    return "";
                }
            }
        }
        return prefix;
    }
}
