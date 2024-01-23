public class Solution {
    public String serialize(String[] A) {
        StringBuilder serializedString = new StringBuilder();
        
        for (String str : A) {
            serializedString.append(str).append(str.length()).append("~");
        }
        
        return serializedString.toString();
    }
}
